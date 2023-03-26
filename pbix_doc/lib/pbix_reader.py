import sys
import os
from pathlib import Path
from pprint import pprint as pp
import json

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
import lib.reader as reader
import zipfile

class pbix_reader(reader.reader):

    def __init__(self, conn, logger):
        
        # Configuration to variables
        self.logger = logger
        self.conn = conn
        self.pbix = {}
        self.pbix_file = conn['file']

    def read_metadata(self):
        pass

    def read_pbix(self, file):
        with zipfile.ZipFile(file, "r") as zip_file:
            ret = {}

            # read file as bytestring
            #ret['data_mashup'] = zip_file.read("DataMashup")
            #ret['report'] = zip_file.read("Report")
            #ret['diagram_state'] = zip_file.read("DiagramState")
            ret['data_model'] = (zip_file.read("DataModel")).decode('utf-8')
            #ret['metadata'] = zip_file.read("Metadata")
            #ret['security_bindings'] = (bytes(zip_file.read("SecurityBindings")))
            
            #ret['version'] =  json.loads((zip_file.read("Version")).decode('utf-16 le'))
            #ret['layout'] = json.loads((zip_file.read("Report/Layout")).decode('utf-16 le'))
            #ret['setting'] = json.loads((zip_file.read("Settings")).decode('utf-16 le'))
            #ret['diagram_layout'] = json.loads((zip_file.read("DiagramLayout")).decode('utf-16 le'))

            #pp(ret['data_model'].keys())
            pp(ret,width=5, depth=2, indent=4) 


#            for k in ret.keys():
#               print(k) 
#             print(pok.keys())


            #settings = zip_file.read("Settings")
            # decode to utf-8
            #setting_text = setting.decode("utf-8")
            # Vytisknout setting_text
            #print(setting_text)
            return ret 
'''
DataModel: Soubor, který obsahuje data a metadat modelu Power BI. Může být ve formátu MSMD (Multidimensional Expressions) nebo ABF (Analysis Services Backup File).
Layout: Soubor XML, který definuje uspořádání a vizualizace reportu Power BI.
Report: Soubor JSON, který obsahuje nastavení reportu Power BI.
Settings: Soubor XML, který obsahuje informace o verzi a konfiguraci souboru PBIX.
Connections: Složka, která obsahuje soubory XML pro každé datové připojení použité v reportu Power BI.
# extract data to temporary directory
    with tempfile.TemporaryDirectory() as tempdir:
        with ZipFile(pbit_path, "r") as pbit:
            for info in pbit.infolist():
                if info.filename == "DataModelSchema":
                    filepath = Path(tempdir, info.filename)
                    pbit.extract(info, tempdir)
                    # read data as utf-8
                    with open(filepath, "r") as _fh:
                        data = json.loads(bytes(_fh.read(), "utf-8"))
                        if data:
                            return data


# https://www.biinsight.com/four-different-ways-to-find-your-power-bi-desktop-local-port-number/#more-5347
# https://www.biinsight.com/connect-to-power-bi-desktop-model-from-excel-and-ssms/

zm1@zm1:/mnt/c/Users/zm1/Microsoft/Power BI Desktop Store App/AnalysisServicesWorkspaces$ find | grep  msmdsrv.port.txt
./AnalysisServicesWorkspace_835ed2bc-a8d8-4409-bdf4-6170420b1763/Data/msmdsrv.port.txt
./AnalysisServicesWorkspace_cf5f3f66-7a36-47eb-91ab-4ee0dc9c1793/Data/msmdsrv.port.txt

folder with pbix
test folder with ssas
run PBI Desktop
connect to Localhost
get metadata
* table 
* reports
get data
write md 
https://www.youtube.com/watch?v=nV7CkMez018

select * from $SYSTEM.DBSCHEMA_CATALOGS
select * // Generated DAX Query
EVALUATE 
TOPN( 500, Customer )
from $SYSTEM.TMSCHEMA_TABLES






'''