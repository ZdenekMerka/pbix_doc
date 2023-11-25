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


class pbix_writer2(writer.writer):

    def __init__(self, pbix_info, output_type ):
        # Configuration to variables
        self.output_type = output_type
        self.pbix_info = pbix_info
        self.template_dir = './conf/templates/' + self.output_type
        self.tmpl = dict()
        self.templates = {
            'properties': 'properties.md',
            'tables': 'tables.md',
            'columns':       'columns.md',
            'relationships': 'relationships.md',
            'measures':      'measures.md',
            'hierarchies':   'hierarchies.md',
            'footer':        'footer.md',
            'index':        'index.md',
            #'breadcrumb':    'breadcrumb.md'
        }

        #self.metadata = metadata
        #self.data = data 
        self.tmpl = dict()
        self.git_version = tools.get_short_git_hash()
        self.logger = logging.getLogger(__name__)
    
    def write_metadata(self):
        pp(self.metadata)

    def init_templates(self):
        # init env 
        self.env = tools.init_templ_env(self.template_dir)
        
        # load all templates from conf 
        for tmpl in self.templates.keys():
            pp(tmpl)
            self.tmpl[tmpl] = self.env.get_template(self.templates[tmpl])
        
        return  self.tmpl


    def render_index(self):
        
        # get data from catalog 
        #pp(self.metadata['TMSCHEMA_MEASURES'])
        
        print(self.tmpl['index'].render(
            index = 'INDEX',
            header = 'HEADER',
            TOC = 'TOC',
            file_type = 'FILETYPE',
            content = 'CONTENT',
            views = 'VIEW',
            footer = 'FOOTER',
            #measures = self.metadata['TMSCHEMA_COLUMNS'].values(),
            ))




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
        # init env 
        self.env = tools.init_templ_env(self.output_conf['template_folder'])
        
        # load all templates from conf 
        for tmpl in self.output_conf[output_type].keys():
            #pp(tmpl)
            #pp(self.output_conf[output_type][tmpl])
            self.tmpl[tmpl] = self.env.get_template(self.output_conf[output_type][tmpl])

    def render_property(self):
        params = dict()
        
        # get data from catalog 
        params.update(self.metadata['DBSCHEMA_CATALOGS'][list(self.metadata['DBSCHEMA_CATALOGS'].keys())[0]])

        # get data from properties 
        for key in self.metadata['DISCOVER_PROPERTIES'].keys():
            #print(f"{key} vs {self.metadata['DISCOVER_PROPERTIES'][key]['Value']}")
            params[key] = self.metadata['DISCOVER_PROPERTIES'][key]['Value']
    
        pp(params)
        
        print(self.tmpl['properties'].render(
            properties = params
            ))

    def render_tables(self):
        
        # get data from catalog 
        pp(self.metadata['TMSCHEMA_TABLES'])
        
        print(self.tmpl['tables'].render(
            tables = self.metadata['TMSCHEMA_TABLES'].values(),
            ))


    def render_columns(self):
        
        # get data from catalog 
        pp(self.metadata['TMSCHEMA_COLUMNS'])
        
        print(self.tmpl['columns'].render(
            columns = self.metadata['TMSCHEMA_COLUMNS'].values(),
            ))
    
    def render_measures(self):
        
        # get data from catalog 
        pp(self.metadata['TMSCHEMA_MEASURES'])
        
        print(self.tmpl['measures'].render(
            measures = self.metadata['TMSCHEMA_COLUMNS'].values(),
            ))
    
    def render_hierarchies(self):
        
        # get data from catalog 
        pp(self.metadata['TMSCHEMA_HIERARCHIES'])
        
        print(self.tmpl['hierarchies'].render(
            hierarchies = self.metadata['TMSCHEMA_HIERARCHIES'].values(),
            ))
    
    def render_relationships(self):
        
        # get data from catalog 
        pp(self.metadata['TMSCHEMA_RELATIONSHIPS'])
        
        print(self.tmpl['relationships'].render(
            relationships = self.metadata['TMSCHEMA_RELATIONSHIPS'].values(),
            ))