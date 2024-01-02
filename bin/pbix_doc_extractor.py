############################################################
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
# python .\bin\pbix_doc_extractor.py --pbix_file ./input/AdventureWorks_Sales.pbix

import os
import sys
import argparse
from datetime import datetime, timedelta
from pprint import pprint as pp
import json

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

# import pbix_doc classes
import lib.conf as cnf
import lib.tools as tools
import lib.pbix_reader as r


####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
parser = argparse.ArgumentParser(description='Get metadata and data info from running pbix file instancies in Power BI Desktop and write them into json file.')
#parser.add_argument('--pbix_file', type=str, required=False, default='xxx', help="PBIX file")
parser.add_argument('--out_file', type=str, required=False, default='data.json', help="Output JSON File with extracted metadata (default = ./data.json)")
#parser.add_argument('--run_pbix', type=str, required=False, default=False, help="No run pbix file (default = False")

args = parser.parse_args()

####################
# load conf 
common_conf = cnf.get_conf('./conf/pbix_doc.yaml')
local_ssas_folder = common_conf['local_ssas_folder']
extractor_version = '1.01'

####################
# init logger
import logging
tools.setup_root_logger(common_conf['log_file'])
logger = logging.getLogger(__name__)


####################
# run power bi

###################
# Open pbix files 
#if (args.run_pbix):
#    tools.open_file_with_default_program1(args.pbix_file)

####################
# collect data from folder
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
    
    ####################
    # collect data from ssas service
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
    #pp(instance_md[md_root].keys())
    
    ############################## 
    # TODO load data statistic


    ############################## 
    # load data from ZIP file
    #pp(pbix_full_path)
    pbix_zip = reader.read_pbix(pbix_full_path)
    parsed_section = reader.parse_visualizations(pbix_zip['layout'])
    #pp(pbix_zip.keys())
    # add zip file information
    instance_md[md_root]['extractor_version'] = extractor_version
    instance_md[md_root]['datetime_extracted'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    instance_md[md_root]['zip_file'] = pbix_zip
    instance_md[md_root]['zip_file']['layout2'] = parsed_section 
    #pp(instance_md[md_root]['zip_file'].keys())



###################
# write to file 
# TODO load file and replace it

tools.save_to_json(instance_md,args.out_file,'./')


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