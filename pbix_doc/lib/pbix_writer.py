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

    def parse_visualizations(self, layout):
        """
        Parses JSON data and extracts information about each visualization section, including
        the section name, the types of visualizations used, the entities used in each visualization,
        and the names of selected items for each visualization.

        Args:
            json_data (str): JSON string to parse.

        Returns:
            dict: Dictionary where each key is the name of a visualization section, and the value is a
            list of dictionaries representing the visualizations in that section. Each visualization dictionary
            contains the following keys:
            - "type": The type of visualization used.
            - "entities": A list of entities used in the visualization.
            - "selected_items": A list of selected items for the visualization (if applicable).
        """
        # Parse JSON data into a Python dictionary.

        # Initialize a dictionary to hold the parsed visualizations.
        visualizations = {}

        # Iterate over each section in the data.
        for section in layout["sections"]:
            # Get the name of the section.
            section_name = section["name"]

            # Initialize a list to hold the visualizations in this section.
            section_visualizations = []

            # Iterate over each visual container in the section.
            for container in section["visualContainers"]:
                pp('XXXXXXXXXXXXXXXXXXXX')
                pp(container['config'])
                pp(type(container['config']))
                visual = json.loads(container['config'])
                try:
                    # Get the visualization type.
                    visual_type = visual["singleVisual"]["visualType"]

                    # Get the entities used in the visualization.
                    entities = []
                    for entity in visual["singleVisual"]["prototypeQuery"]["From"]:
                        entities.append(entity["Entity"])

                    # Get the selected items (if applicable).
                    selected_items = []
                    for item in visual["singleVisual"]["prototypeQuery"]["Select"]:
                        selected_items.append(item.get("Name", ""))

                    # Add the parsed visualization to the list for this section.
                    section_visualizations.append({
                        "type": visual_type,
                        "entities": entities,
                        "selected_items": selected_items
                    })
                except KeyError:
                    # Skip this container if there is no prototypeQuery (which contains the required data).
                    continue

            # Add the list of parsed visualizations to the dictionary for this section.
            visualizations[section_name] = section_visualizations

        return visualizations