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

def get_visual_config_info(config):
    ret = dict()
    ret["name"] = config['name']
    ret["type"] = config["singleVisual"]["visualType"]
    
    # some old code 
    try:
        # Get the visualization type.

        # Get the entities used in the visualization.
        entities = []
        for entity in config["singleVisual"]["prototypeQuery"]["From"]:
            entities.append(entity["Entity"])

        # Get the selected items (if applicable).
        selected_items = []
        for item in config["singleVisual"]["prototypeQuery"]["Select"]:
            name = item.get("Name",'')
            keys = list(item.keys())
            keys.remove("Name")
            first_key = keys[0]
            #selected_items.append({'name':name, 'type':first_key})
            selected_items.append(f"{first_key}: {name}")


        # Add the parsed visualization to the list for this section.
        ret["entities"] = entities
        ret["selected_items"] = selected_items
    except KeyError:
        # Skip this container if there is no prototypeQuery (which contains the required data).
        ret["entities"] = ['n/a']
        ret["selected_items"] = ['n/a']
        #pass

    return ret 

class pbix_writer2(writer.writer):

    def __init__(self, pbix_data, output_type ):
        # Configuration to variables
        self.output_type = output_type
        self.pbix_data = pbix_data
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
            'index':         'index.md',
            'pbix_doc':      'pbix_doc.md',
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
        # init jinja2 env 
        self.env = tools.init_templ_env( self.template_dir)
        self.env.globals['str'] = str
        self.env.globals['str_slicer'] = tools.str_slicer
        self.env.globals['re_nan'] = tools.remove_nan
        self.env.globals['len'] = len
        #self.env.globals['json_load'] = json.load
        self.env.globals['type'] = type
        self.env.globals['get_visual_config_info'] = get_visual_config_info
        self.env.globals['join'] = ', '.join
        self.env.globals['joinnl'] = '<br/> '.join


        # load all templates from conf 
        for tmpl in self.templates.keys():
            pp(tmpl)
            self.tmpl[tmpl] = self.env.get_template(self.templates[tmpl])
        
        return  self.tmpl

    
    def render_pbix_doc(self):

        #tables_idx = self.pbix_data["ssas_md"]['TMSCHEMA_TABLES']
        #columns_idx  = self.pbix_data['ssas_md']['TMSCHEMA_COLUMNS']
        #pp( json.loads(self.pbix_data['zip_file']['layout']['sections'][0]['visualContainers'][0]['config']))
        
        ret =self.tmpl['pbix_doc'].render(
            properties =  self.pbix_data["ssas_md"]["DBSCHEMA_CATALOGS"][self.pbix_data['info']['catalog']],
            git_version = self.git_version,
            port = self.pbix_data['info']['port'],
            filename = os.path.basename(self.pbix_data['info']['pbix_full_path']),
            full_filename = self.pbix_data['info']['pbix_full_path'],
            tables = self.pbix_data["ssas_md"]['TMSCHEMA_TABLES'].values(),
            tables_idx  = self.pbix_data["ssas_md"]['TMSCHEMA_TABLES'],
            columns  = self.pbix_data['ssas_md']['TMSCHEMA_COLUMNS'].values(),
            columns_idx  = self.pbix_data['ssas_md']['TMSCHEMA_COLUMNS'],
            measures =      self.pbix_data['ssas_md']['TMSCHEMA_COLUMNS'].values(),
            relationships = self.pbix_data['ssas_md']['TMSCHEMA_RELATIONSHIPS'].values(),
            hierarchies =   self.pbix_data['ssas_md']['TMSCHEMA_HIERARCHIES'].values(),
            report_sections = self.pbix_data['zip_file']['layout']['sections'],


            )
        return ret

    def render_index(self, filenames_pbix):

        ret =self.tmpl['index'].render(
            filenames_pbix =  filenames_pbix,
            git_version = self.git_version,
            )
        return ret



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
