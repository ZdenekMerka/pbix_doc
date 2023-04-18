import sys
import os
from pathlib import Path
from sys import path
import logging
from pprint import pprint as pp
import pandas as pd
import json

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.reader as reader
import lib.tools as tools
import zipfile

class pbix_reader(reader.reader):
    
    def __init__(self, server, port, catalog, adomd_path):
        self.server = server
        self.port = port
        self.catalog = catalog
        self.adomd_path = adomd_path
        self.cache = dict()
        self.logger = logging.getLogger(__name__)
        # connection_string = 'Provider='+conf['driver']+';Data Source='+conf['server']+';Catalog='+conf['database']+';'
        self.conn_str = f'Provider=MSOLAP;Data Source={server}:{port};Initial Catalog={catalog};'
        self.logger.info(f"Try to connect SSAS with this connection string {self.conn_str}")
        #pp(self.conn_str)

        #############################  
        # connect:
        #added to the path _before_ importing the pyadomd package
        try:
            path.append(self.adomd_path)
            #pp(path)
            from pyadomd import Pyadomd
            self.conn = Pyadomd(self.conn_str)
            self.logger.info(f'Connected to SSAS {self.catalog}')
        except Exception as e:
            self.logger('Connection SSAS {} failed: {}'.format(self.catalog,str(e)))


    ############################################################
    # function
    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.logger.info('Disconnected from SSAS {}'.format(self.catalog))

    ############################################################
    # function
    from retrying import retry
    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def query(self, query_str):
        cache_key = tools._cache_key_gen(query_str)
        self.logger.info(query_str + ' BEGIN.')
        
        if cache_key not in self.cache.keys():
            self.logger.info(query_str +' CACHE DIDNT HIT.')

            if self.conn:
                try:
                    with self.conn as conn:
                        result = pd.read_sql(sql=query_str, con=conn)
                    #df = pd.read_sql(query_str, self.conn)
                    self.cache[cache_key] = result
                except Exception as e:
                    self.logger.info('Query failed on catalog {} with exception {}'.format(self.catalog, str(e)))
            else:
                self.logger.info(f'Not connected to SSAS catalog {self.catalog}')

        else:
            self.logger.info(query_str +' CACHE WAS HIT.')
        ret = self.cache.get(cache_key)
        return ret

    ############################################################
    # function
    def query_gpt(self, query_str, params=None):
        # Generate cache key using the query string
        cache_key = tools._cache_key_gen(query_str,params)
        # Log the start of the query
        self.logger.info(f'BEGIN. {query_str} with {params}')
        
        # Check if the result is already cached
        if cache_key not in self.cache.keys():
            # If the result is not cached, execute the query
            self.logger.info(query_str +' CACHE DIDNT HIT.')
            
            # Check if the connection to the database is open
            if self.conn:
                try:
                    # Use the connection to execute the query and store the result in a DataFrame
                    with self.conn as conn:
                        result = pd.read_sql(sql=query_str, con=conn,  params=params)
                    # Cache the result
                    self.cache[cache_key] = result
                except Exception as e:
                    # Log an error message if the query fails
                    self.logger.info('Query failed on catalog {} with exception {}'.format(self.catalog, str(e)))
                    exit(1)
            else:
                # Log a message if the connection to the database is not open
                self.logger.info(f'Not connected to SSAS catalog {self.catalog}')

        else:
            # If the result is already cached, log a message
            self.logger.info(query_str +' CACHE WAS HIT.')
        # Return the cached result
        ret = self.cache.get(cache_key)
        return ret




    ############################################################
    # function
    def read_metadata(self,pbix_tables, pbix_table_prefix, catalog ):
        ret =  {}
        for ref in pbix_tables:
            tab = ref['table']
            idx = ref['idx']
            #sql = f'SELECT TOP 10000 * FROM {pbix_table_prefix}.{tab}'
            sql = f'SELECT * FROM {pbix_table_prefix}.{tab}'
            #self.logger.info(sql)
            df_result = self.query(sql)
            ret[tab] = tools.df2dictofdictsref(df_result,idx) 
            
            # write file 
            tools.save_df_to_yaml(df_result,f'{tab.lower()}.yaml',catalog)
            tools.save_df_to_json(df_result,f'{tab.lower()}.json',catalog)
            tools.save_df_to_excel(df_result,f'{tab.lower()}.xlsx',catalog)
            
        return ret

    ############################################################
    # md_get_tables
    ###############################
    def md_get_tables(self):
        sql='''select * from $SYSTEM.TMSCHEMA_TABLES'''
        self.logger.info("Getting all tables from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Table')
        return ret

    ############################################################
    # md_get_roles
    ###############################
    def md_get_roles(self):
        sql='''select * from $SYSTEM.TMSCHEMA_ROLES'''
        self.logger.info("Getting all roles from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Role')
        return ret

    ############################################################
    # md_get_relationships
    ###############################
    def md_get_relationships(self):
        sql='''select * from $SYSTEM.TMSCHEMA_RELATIONSHIPS'''
        self.logger.info("Getting all relationships from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Relationship')
        return ret

    ############################################################
    # md_get_measures
    ###############################
    def md_get_measures(self):
        sql='''select * from $SYSTEM.TMSCHEMA_MEASURES'''
        self.logger.info("Getting all measures from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Measure')
        return ret

    ############################################################
    # md_get_kpis
    ###############################
    def md_get_kpis(self):
        sql='''select * from $SYSTEM.TMSCHEMA_KPIS'''
        self.logger.info("Getting all KPIs from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='KPI')
        return ret

    ############################################################
    # md_get_hierarchies
    ###############################
    def md_get_hierarchies(self):
        sql='''select * from $SYSTEM.TMSCHEMA_HIERARCHIES'''
        self.logger.info("Getting all hierarchies from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Hierarchy')
        return ret

    ############################################################
    # md_get_datasource
    ###############################
    def md_get_datasource(self):
        sql='''select * from $SYSTEM.TMSCHEMA_DATA_SOURCES'''
        self.logger.info("Getting all datasource from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Datasource')
        return ret
        
    ############################################################
    # md_get_columns
    ###############################
    def md_get_columns(self):
        sql='''select * from $SYSTEM.TMSCHEMA_COLUMNS'''
        self.logger.info("Getting all columns from SSAS")
        ret = tools.sql2pandas(self.query(sql),params='Column')
        return ret


