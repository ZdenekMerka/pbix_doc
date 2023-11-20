import yaml
import os

current_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..\\')

##############################
##########


def get_conf(file_path=None):
    #if file_path is None:
    #    file_path = current_folder + "conf\common.yaml"

    #print(file_path)
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def get_connections(file_path=None):
    #if file_path is None:
        #file_path = current_folder + "conf\connections.yaml"

    with open(file_path, "r") as f:
        return yaml.safe_load(f)
