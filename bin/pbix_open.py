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
# python .\bin\pbix_open.py --pbix_folder

import os
import sys
from pprint import pprint as pp
import argparse
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.tools as tools
import lib.conf as cnf

####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
# arg parse 
parser = argparse.ArgumentParser(description='Open pbix files from defined folder.')
parser.add_argument('--pbix_folder', type=str, required=True, default='./', help="Run all pbix files in given folder. (default = ./)")
parser.add_argument('--log_file', type=str, required=False, default='./tmp/pbix.open.log', help="Log file. (default = ./tmp/pbix.open.log)")
parser.add_argument('--conf_file', type=str, required=False, default='conf/common.yaml', help="YAML File with project configurations (default = ./conf/common.yaml)")

args = parser.parse_args()

####################
# load conf 
common_conf = cnf.get_conf(args.conf_file)
pbix_folder = args.pbix_folder
pp(pbix_folder)

####################
# init logger
import logging
tools.setup_root_logger(args.log_file)
logger = logging.getLogger(__name__)

###################
# get pbix file from folder
pbix_files = tools.get_all_pbix_files(pbix_folder)

###################
# Open pbix files 
for file in pbix_files:
    tools.open_file_with_default_program1(file)

###################
# get ssas folders
ssas_folders = tools.get_first_level_subfolders(common_conf['local_ssas_folder'])

pp(ssas_folders)

###################
# get ssas poart 
for i in ssas_folders:
    pp(tools.get_port_and_db(i))



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