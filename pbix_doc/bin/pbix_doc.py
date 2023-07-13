# 
# Copyright (C) 2023 Zdenek Merka
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
import lib.pbix_writer as w



####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
# arg parse 
parser = argparse.ArgumentParser(description='Get metadata info from given datasource and write them into Markdown files.')
parser.add_argument('--conf_file', type=str, required=False, default='conf/common.yaml', help="YAML File with project configurations (default = ./conf/common.yaml)")
parser.add_argument('--md_out_file', type=str, required=False, default='md.json', help="Output JSON File with extracted/appeneded metadata (default = ./md.json)")
#parser.add_argument("--out", "--output", type=str, action='store', required=False, help="Define path for output files.")
#parser.add_argument("--conn_id", type=str, action='store', required=True, help="Define connection from connection conf file.")
#parser.add_argument("--top", type=int, action='store', required=False, help="Set how many top rows you want to get.")
#parser.add_argument("--append", action='store_true', required=False, help="Use if you want to append new documentation to existing one. Argument is name of new generated output.")
#parser.add_argument("--link_name", type=str, action='store', required=False, help="Use if you want to replace auto generating name of DB.")

args = parser.parse_args()

####################
# load conf 
common_conf = cnf.get_conf(args.conf_file)
local_ssas_folder = common_conf['local_ssas_folder']
#pp(common_conf)


pbix_files = cnf.get_conf('conf/connections.yaml')
#pp(pbix_files)
####################
# init logger
import logging
tools.setup_root_logger(common_conf['log_file'])
logger = logging.getLogger(__name__)

###################
# get ssas instancies
ssas_instancie_folders = tools.get_first_level_subfolders(local_ssas_folder)
pp(ssas_instancie_folders)
instance_md = dict()
for instance_folder in ssas_instancie_folders:

    # get pbix file name    
    pbix_full_path = tools.get_pbix_filename_from_trc(f"{instance_folder}\{common_conf['trc_file_rel_path']}")
    if not pbix_full_path:
        pbix_full_path = tools.get_pbix_filename_from_trc(f"{instance_folder}\{common_conf['trc_back_file_rel_path']}")
    
    md_root = os.path.basename(pbix_full_path)
    instance_md.setdefault(md_root, {}).setdefault("info", {})["pbix_full_path"] = pbix_full_path

    
    # get port and catalog 
    ssas_instance_params = tools.get_port_and_db(instance_folder)
    port = ssas_instance_params[0] 
    catalog = ssas_instance_params[1]
    instance_md[md_root]['info']['port'] = port
    instance_md[md_root]['info']['catalog'] = catalog
    # TODO add date time of generation
    


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
    
    # add ssas information
    instance_md[md_root]['ssas_md'] = tools.convert_timestamps_to_string(md)
    pp(instance_md[md_root].keys())
    
    ############################## 
    # TODO load data statistic
    
 
    ############################## 
    # load data from ZIP file
    pp(pbix_full_path)
    pbix_zip = reader.read_pbix(pbix_full_path)
    pp(reader.parse_visualizations(pbix_zip['layout']))
    pp(pbix_zip.keys())
    # add zip file information
    instance_md[md_root]['zip_file'] = pbix_zip
    #pp(instance_md[md_root]['zip_file'].keys())


    #pp(md)
#    ###################
#    # init writer 
#    writer =  w.pbix_writer(md,None, common_conf['output'])
#    writer.init_templates()
#    #writer.render_property()
#    #writer.render_tables()
#    #writer.render_columns()
#    #writer.render_measures()
#    #writer.render_hierarchies()
#    writer.render_relationships()
#    #writer.write_metadata()



###################
# write to file 
# TODO load file and replace it

tools.save_to_json(instance_md,args.md_out_file,'./')





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