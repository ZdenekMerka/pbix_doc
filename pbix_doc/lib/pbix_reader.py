import sys
import os
from pathlib import Path
from pprint import pprint as pp

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.reader as reader

class pbix_reader(reader.reader):

    def __init__(self, conf, logging, environment, common_conf, metadata_conf):
        # Configuration to variables
        self.to_html = used_conf['To-html']
        self.to_pdf = used_conf['To-pdf']
        self.select_top = used_conf['Select Top']
        self.dbi = dbi
        self.logger = self.dbi.logger
        self.conn = conn
        self.project_path = used_conf['Project path']
        self.ignored_schemas = used_conf['Ignored schemas']
        self.ignored_objects = used_conf['Ignored objects']
        self.logging = logging
        self.environment = environment
        self.common_conf = common_conf
        self.metadata_conf = metadata_conf
        self.used_conf = used_conf
        if used_conf['Schemas'] == "All schemas":
            self.requested_schemas = None
        else:
            self.requested_schemas = used_conf['Schemas']



# Importovat modul zipfile
import zipfile

# Otevřít soubor pbix jako zip soubor
with zipfile.ZipFile("soubor.pbix", "r") as zip_file:

    # Načíst soubor DataMashup jako bytestring
    data_mashup = zip_file.read("DataMashup")

    # Načíst soubor Report jako bytestring
    report = zip_file.read("Report")

    # Načíst soubor Settings jako bytestring
    settings = zip_file.read("Settings")

    # Načíst soubor DiagramState jako bytestring
    diagram_state = zip_file.read("DiagramState")

    # Načíst soubor Metadata jako bytestring
    metadata = zip_file.read("Metadata")

    # Načíst soubor SecurityBindings jako bytestring
    security_bindings = zip_file.read("SecurityBindings")

    # Načíst soubor Version jako bytestring
    version = zip_file.read("Version")


    # Dekódovat setting jako řetězec s kódováním utf-8
    setting_text = setting.decode("utf-8")

    # Vytisknout setting_text
    print(setting_text)