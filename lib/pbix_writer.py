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
    
    # some old code 
    try:
        # Get the visualization type.
        ret["type"] = config["singleVisual"]["visualType"]

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
        ret["type"] = ['n/a']
        #pass

    return ret 

class pbix_writer(writer.writer):

    def __init__(self, pbix_data, output_type ):
        # Configuration to variables
        self.output_type = output_type
        self.pbix_data = pbix_data
        self.template_dir = './conf/templates/' + self.output_type
        self.templates = {
            'footer':        'footer.md',
            'index':         'index.md',
            'pbix_doc_dmv':   'pbix_doc_dmv.md',
            'pbix_doc_report': 'pbix_doc_report.md',
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
        self.env.globals['render_filters'] = render_filters
        self.env.globals['parse_filters'] = tools.parse_filters
        
        import urllib.parse
        self.env.globals['urlquote'] = urllib.parse.quote



        # load all templates from conf 
        for tmpl in self.templates.keys():
            #pp(tmpl)
            self.tmpl[tmpl] = self.env.get_template(self.templates[tmpl])
        
        return  self.tmpl

    
    def render_pbix_doc(self):

        #tables_idx = self.pbix_data["ssas_md"]['TMSCHEMA_TABLES']
        #columns_idx  = self.pbix_data['ssas_md']['TMSCHEMA_COLUMNS']
        #pp( json.loads(self.pbix_data['zip_file']['layout']['sections'][0]['visualContainers'][0]['config']))
        
        ret =self.tmpl['pbix_doc_dmv'].render(
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
            #report_sections = self.pbix_data['zip_file']['layout']['sections'],


            )
        return ret
    
    def get_tables_global(self):
        filename = os.path.basename(self.pbix_data['info']['pbix_full_path'])
        global_tables = self.pbix_data["ssas_md"]['TMSCHEMA_TABLES']

        ret = []
        for key, values in global_tables.items():
            values['filename'] = filename
            ret.append(values)

        return list(ret)
    
    def render_pbix_doc_report(self):
        """
        Renders the Power BI report document using the template 'pbix_doc_report'.
        
        Returns:
            str: The rendered Power BI report document.
        """

        ret =self.tmpl['pbix_doc_report'].render(
            filename = os.path.basename(self.pbix_data['info']['pbix_full_path']),
            report_sections = self.pbix_data['zip_file']['layout']['sections'],
            )
        return ret

class pbix_writer_global():
    def __init__(self,  output_type ):
        # Configuration to variables
        self.output_type = output_type
        self.template_dir = './conf/templates/' + self.output_type
        self.templates = {
            'index': 'index.md',
            'bas':   'bas.md',
        }

        self.tmpl = dict()
        self.git_version = tools.get_short_git_hash()
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Class {__name__} was inicialized.")

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
        
        import urllib.parse
        self.env.globals['urlquote'] = urllib.parse.quote

        # load all templates from conf 
        for tmpl in self.templates.keys():
            #pp(tmpl)
            self.tmpl[tmpl] = self.env.get_template(self.templates[tmpl])
        
        self.logger.info(f"Templates {__name__} inicialized.")
        return  self.tmpl

    def render_index(self, filenames_pbix):

        self.logger.info(f"Going render index page.")
        ret =self.tmpl['index'].render(
            filenames_pbix =  filenames_pbix,
            git_version = self.git_version,
            )
        return ret

    def render_bas(self, tables_global):

        self.logger.info(f"Going sort bas page.")
        from operator import itemgetter
        tables_global_sorted = sorted(tables_global, key=itemgetter('Name', 'filename'))

        self.logger.info(f"Going render bas page.")
        ret =self.tmpl['bas'].render(
            tables_global =  tables_global_sorted,
            git_version = self.git_version,
            )
        return ret

def render_filters(filters):
    """
    Render a list of filters into a Markdown formatted string.

    Args:
        filters (list): A list of dictionaries representing filters. Each dictionary
            should have the following keys:
            - name (str): The name of the filter.
            - type (str): The type of the filter.
            - columns (list): A list of columns used by the filter.
            - filter (dict): A dictionary representing the filter expression.

    Returns:
        str: A Markdown formatted string containing the filter information. Each filter
            is represented as a line in the string with the following format:
            "Name: `{filter['name']}` Type: `{filter['type']}` Column: `{', '.join(filter['columns'])}` [<sup>def</sup>](## '{json.dumps(filter['filter'])}')"
    """
    ret = []
    for filter in filters:
        dump = json.dumps(filter['filter']).replace("'", "\\'")
        ret.append(fr"Name: `{filter['name']}` Type: `{filter['type']}` Column: `{', '.join(filter['columns'])}` [<sup>def</sup>](## '{dump}')")
    return "<br/>".join(ret) 
    # | **Filters** | `table.column`[<sup>?</sup>](## '{"From": [{"Entity": "Countries", "Name": "c", "Type": 0}], "Version": 2, "Where": [{"Condition": {"Not": {"Expression": {"In": {"Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "c"}}, "Property": "Country"}}], "Values": [[{"Literal": {"Value": "null"}}]]}}}}}]}') |

