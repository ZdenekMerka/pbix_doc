import os
import sys
import pandas as pd
#import numpy as np
from pprint import pprint as pp
import argparse
import jinja2 as jj 
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.conf as cnf

# import functional classes
#import lib.pbix_reader as pbixr
#import lib.pbix_writer as pbixw

import logging

####################
# save script starting time
start_time = datetime.now()

####################
# arg parse 
# arg parse 
parser = argparse.ArgumentParser(description='Get metadata info from given datasource and write them into Markdown files.')
parser.add_argument('--conf_file', type=str, required=False, default='conf/common.yaml', help="YAML File with project configurations (default = ./conf/common.yaml)")
parser.add_argument("--out", "--output", type=str, action='store', required=False, help="Define path for output files.")
parser.add_argument("--db_id", type=str, action='store', required=True, help="Define connection from connection to db in connection conf file.")
parser.add_argument("--top", type=int, action='store', required=False, help="Set how many top rows you want to get.")
parser.add_argument("--append", action='store_true', required=False, help="Use if you want to append new documentation to existing one. Argument is name of new generated output.")
parser.add_argument("--link_name", type=str, action='store', required=False, help="Use if you want to replace auto generating name of DB.")

args = parser.parse_args()

####################
# load conf 
common_conf = cnf.get_conf(args.conf_file)

##############################
# measure script run time before last page writing
end_time = datetime.now()

# vypočítáme hodiny, minuty a sekundy
lasting = end_time - start_time

# convert timedelta to 0h 55m 22s format
lasting = ("%sh %sm %ss" % (tuple(str(lasting).split('.')[0].split(':'))) )

##############################
# measure script run time
print("Done. It took {}".format(lasting) )