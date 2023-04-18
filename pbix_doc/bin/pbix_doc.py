##############################
# how to run 
# python .\bin\pbix_doc.py --conn_id aw_sales

import os
import sys
import pandas as pd
#import numpy as np
from pprint import pprint as pp
import argparse
import jinja2 as jj 
from datetime import datetime, timedelta
import time 

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.conf as cnf
import lib.tools as tools

# import functional classes
import lib.pbix_reader as r
#import lib.pbix_writer as w



####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
# arg parse 
parser = argparse.ArgumentParser(description='Get metadata info from given datasource and write them into Markdown files.')
parser.add_argument('--conf_file', type=str, required=False, default='conf/common.yaml', help="YAML File with project configurations (default = ./conf/common.yaml)")
parser.add_argument("--out", "--output", type=str, action='store', required=False, help="Define path for output files.")
#parser.add_argument("--conn_id", type=str, action='store', required=True, help="Define connection from connection conf file.")
#parser.add_argument("--top", type=int, action='store', required=False, help="Set how many top rows you want to get.")
#parser.add_argument("--append", action='store_true', required=False, help="Use if you want to append new documentation to existing one. Argument is name of new generated output.")
#parser.add_argument("--link_name", type=str, action='store', required=False, help="Use if you want to replace auto generating name of DB.")

args = parser.parse_args()

####################
# load conf 
common_conf = cnf.get_conf(args.conf_file)
local_ssas_folder = common_conf['local_ssas_folder']

pp(common_conf)
####################
# init logger
import logging
tools.setup_root_logger(common_conf['log_file'])
logger = logging.getLogger(__name__)

###################
# get ssas instancies
ssas_instancie_folders = tools.get_first_level_subfolders(local_ssas_folder)
for instance_folder in ssas_instancie_folders:
    ssas_instance_params = tools.get_port_and_db(instance_folder)
    port = ssas_instance_params[0] 
    catalog = ssas_instance_params[1]


    ###################
    # init reader
    # create instance of pbix_reader class
    reader =  r.pbix_reader(
        server = 'localhost', 
        port = port, 
        catalog = catalog, 
        adomd_path = common_conf['adomd_path']
        )
    #pp(reader.query('''select * from $SYSTEM.TMSCHEMA_TABLES'''))
    #pp(reader.query('''EVALUATE TOPN( 50, 'Sales Order' )'''))
    pbix_tables = common_conf['all_pbix_tables']
    pbix_table_prefix = common_conf['pbix_table_prefix']
    md = reader.read_metadata(pbix_tables,pbix_table_prefix, catalog) 

    #pp(md)







'''
reader.read_pbix(reader.pbix_file)
my_reader = pbix_reader('your-ssas-server-name', 'your-ssas-catalog-name')

# connect to SSAS
my_reader.connect()

# execute a query
result = my_reader.query('SELECT * FROM your-ssas-table-name')
print(result)

# disconnect from SSAS
my_reader.disconnect()


#reader = pbixr()



'''












##############################
# measure script run time before last page writing
end_time = datetime.now()

# vypočítáme hodiny, minuty a sekundy
lasting = end_time - start_time

# convert timedelta to 0h 55m 22s format
lasting = ("%sh %sm %ss" % (tuple(str(lasting).split('.')[0].split(':'))) )

##############################
# measure script run time
logger.info("Done. It took {}".format(lasting) )