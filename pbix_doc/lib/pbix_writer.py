import sys
import os
from pathlib import Path
from sys import path
import logging
from pprint import pprint as pp
import pandas as pd
import json
from jinja2 import Environment, FileSystemLoader

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.writer as writer
import lib.tools as tools
class pbix_writer(writer.writer):

    def __init__(self, metadata, data, output_conf ):
        # Configuration to variables
        self.metadata = metadata
        self.data = data 
        self.output_conf = output_conf
        self.tmpl = dict()
        self.git_version = tools.get_short_git_hash()
        self.logger = logging.getLogger(__name__)


    def write_metadata(self):
        pp(self.metadata)


    def init_templates(self,output_type = 'md_github'):
        
        self.env = tools.init_templ_env(self.output_conf['template_folder'])
        
        for tmpl in self.output_conf[output_type].keys():
            pp(tmpl)
            pp(self.output_conf[output_type][tmpl])
            self.tmpl[tmpl] = self.env.get_template(self.output_conf[output_type][tmpl])


        pp(self.tmpl['test'].render(
            git_version = self.git_version
            )
        )

'''
            self.tmpl_properties_md = self.environment.get_template("md/properties.md")
            self.tmpl_databases_md = self.environment.get_template("md/databases.md")
            self.tmpl_schemas_md = self.environment.get_template("md/schemas.md")
            self.tmpl_schema_md = self.environment.get_template("md/schema.md")
            self.tmpl_tables_md = self.environment.get_template("md/tables.md")
'''