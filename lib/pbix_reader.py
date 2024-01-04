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
            df_result = df_result.fillna('-NaN-')
            ret[tab] = tools.df2dictofdictsref(df_result,idx) 
            
            # write file for debuging
            # tools.save_df_to_yaml(df_result,f'{tab.lower()}.yaml',catalog)
            # tools.save_df_to_json(df_result,f'{tab.lower()}.json',catalog)
            # tools.save_df_to_excel(df_result,f'{tab.lower()}.xlsx',catalog)
            
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



    def read_pbix(self, file):
        with zipfile.ZipFile(file, "r") as zip_file:
            ret = {}

            # read file as bytestring
            #ret['data_mashup'] = zip_file.read("DataMashup")
            #ret['report'] = zip_file.read("Report")
            #ret['diagram_state'] = zip_file.read("DiagramState")
            #ret['data_model'] = (zip_file.read("DataModel")).decode('utf-8')
            ret['metadata'] = json.loads((zip_file.read("Metadata")).decode('utf-16 le'))
            #ret['security_bindings'] = (bytes(zip_file.read("SecurityBindings")))
            
            ret['version'] =  json.loads((zip_file.read("Version")).decode('utf-16 le'))
            ret['layout'] = json.loads((zip_file.read("Report/Layout")).decode('utf-16 le'))
            ret['setting'] = json.loads((zip_file.read("Settings")).decode('utf-16 le'))
            ret['diagram_layout'] = json.loads((zip_file.read("DiagramLayout")).decode('utf-16 le'))

            #pp(ret['data_model'].keys())
            #pp(ret,width=5, depth=2, indent=4) 
            #pp(ret) 

            # convert the JSON object to a string
            #json_string = json.dumps(ret['layout'])

            # print the JSON string
            #print(json_string)

            #for k in ret['layout'].keys():
               #print(k) 


            #settings = zip_file.read("Settings")
            # decode to utf-8
            #setting_text = setting.decode("utf-8")
            # Vytisknout setting_text
            #print(setting_text)
            return ret 

    def parse_visualizations(self, layout):
        """
        Parses JSON data and extracts information about each visualization section, including
        the section name, the types of visualizations used, the entities used in each visualization,
        and the names of selected items for each visualization.

        Args:
            json_data (str): JSON string to parse.

        Returns:
            dict: Dictionary where each key is the name of a visualization section, and the value is a
            list of dictionaries representing the visualizations in that section. Each visualization dictionary
            contains the following keys:
            - "type": The type of visualization used.
            - "entities": A list of entities used in the visualization.
            - "selected_items": A list of selected items for the visualization (if applicable).
        """
        # Parse JSON data into a Python dictionary.

        # Initialize a dictionary to hold the parsed visualizations.
        visualizations = {}

        # Iterate over each section in the data.
        for section in layout["sections"]:
            # Get the name of the section.
            section_name = section["name"]
            displayName = section["displayName"]

            # Initialize a list to hold the visualizations in this section.
            section_visualizations = []

            # Iterate over each visual container in the section.
            for container in section["visualContainers"]:
                
                visual = json.loads(container['config'])
                
                # decode config, query, dataTransforms, filters                
                if container.get('config') is not None and container.get('config') != '':
                    container['config'] = json.loads(container['config'])

                if container.get('query') is not None and container.get('query') != '':
                    container['query'] = json.loads(container['query'])

                if container.get('dataTransforms') is not None and container.get('dataTransforms') != '':
                    container['dataTransforms'] = json.loads(container['dataTransforms'])
                
                if container.get('filters') is not None and container.get('filters') != '':
                    container['filters'] = json.loads(container['filters'])

                
                
                # some old code 
                try:
                    # Get the visualization type.
                    visual_type = visual["singleVisual"]["visualType"]

                    # Get the entities used in the visualization.
                    entities = []
                    for entity in visual["singleVisual"]["prototypeQuery"]["From"]:
                        entities.append(entity["Entity"])

                    # Get the selected items (if applicable).
                    selected_items = []
                    for item in visual["singleVisual"]["prototypeQuery"]["Select"]:
                        selected_items.append(item.get("Name", ""))

                    # Add the parsed visualization to the list for this section.
                    section_visualizations.append({
                        "type": visual_type,
                        "entities": entities,
                        "selected_items": selected_items
                    })
                except KeyError:
                    # Skip this container if there is no prototypeQuery (which contains the required data).
                    continue

            # Add the list of parsed visualizations to the dictionary for this section.
            visualizations[displayName] = section_visualizations
            

        return visualizations





'''
DataModel: Soubor, který obsahuje data a metadat modelu Power BI. Může být ve formátu MSMD (Multidimensional Expressions) nebo ABF (Analysis Services Backup File).
Layout: Soubor XML, který definuje uspořádání a vizualizace reportu Power BI.
Report: Soubor JSON, který obsahuje nastavení reportu Power BI.
Settings: Soubor XML, který obsahuje informace o verzi a konfiguraci souboru PBIX.
Connections: Složka, která obsahuje soubory XML pro každé datové připojení použité v reportu Power BI.
# extract data to temporary directory
    with tempfile.TemporaryDirectory() as tempdir:
        with ZipFile(pbit_path, "r") as pbit:
            for info in pbit.infolist():
                if info.filename == "DataModelSchema":
                    filepath = Path(tempdir, info.filename)
                    pbit.extract(info, tempdir)
                    # read data as utf-8
                    with open(filepath, "r") as _fh:
                        data = json.loads(bytes(_fh.read(), "utf-8"))
                        if data:
                            return data


# https://www.biinsight.com/four-different-ways-to-find-your-power-bi-desktop-local-port-number/#more-5347
# https://www.biinsight.com/connect-to-power-bi-desktop-model-from-excel-and-ssms/

zm1@zm1:/mnt/c/Users/zm1/Microsoft/Power BI Desktop Store App/AnalysisServicesWorkspaces$ find | grep  msmdsrv.port.txt
./AnalysisServicesWorkspace_835ed2bc-a8d8-4409-bdf4-6170420b1763/Data/msmdsrv.port.txt
./AnalysisServicesWorkspace_cf5f3f66-7a36-47eb-91ab-4ee0dc9c1793/Data/msmdsrv.port.txt

folder with pbix
test folder with ssas
run PBI Desktop
connect to Localhost
get metadata
* table 
* reports
get data
write md 
https://www.youtube.com/watch?v=nV7CkMez018

select * from $SYSTEM.DBSCHEMA_CATALOGS
select * // Generated DAX Query
EVALUATE 
TOPN( 500, Customer )
from $SYSTEM.TMSCHEMA_TABLES
'''
