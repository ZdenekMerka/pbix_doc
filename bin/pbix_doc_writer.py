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
# python .\bin\pbix_doc_writer.py --files ./input/data1.json ./input/data2.json

import os
import sys
import argparse
from datetime import datetime, timedelta
from pprint import pprint as pp

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

# import pbix_doc classes
import lib.conf as cnf
import lib.tools as tools
import lib.pbix_writer as w

####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
parser = argparse.ArgumentParser(description='Render metadata and data info obtained from pbix_doc_extractor write them into requested format.')
parser.add_argument('--files', type=str, nargs='+', required=True,  help='List of files to process')
parser.add_argument('--format', type=str, required=False, default='md', help="Requested output format")
parser.add_argument('--out_dir', type=str, required=False, default='./output', help="Output dir (default ./output).")


args = parser.parse_args()

jsons = tools.read_jsons(args.files) 

for json_key in jsons.keys():
    for file_name_key in jsons[json_key].keys():
        print(json_key)
        print(file_name_key)

        ###################
    #    # init writer 
        writer = w.pbix_writer2(jsons[json_key][file_name_key],  args.format)
        pp(writer.templates)
        pp(writer.init_templates())
        content = writer.render_index()
        tools.write_file(
            filename = '{dir}/{filename}.{ext}'.format(
                dir = args.out_dir,
                filename = os.path.basename(jsons[json_key][file_name_key]['info']['pbix_full_path']),
                ext = 'md'),         
            content = content  
        )



#    #writer.render_property()
#    #writer.render_tables()
#    #writer.render_columns()
#    #writer.render_measures()
#    #writer.render_hierarchies()
#    writer.render_relationships()
#    #writer.write_metadata()
# file name with extension
file_name = os.path.basename('/root/file.ext')
