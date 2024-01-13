from pprint import pprint as pp
import os
import logging
import time
import re

############################################################
# function
def read_jsons(filenames):
    """
    Reads all JSON files from the list `filenames` and returns them in
    a key/value structure, where the key is the file name and the value is its
    content.

    Args:
        filenames: List of JSON file names.

    Returns:
        Key/value structure, where the key is the file name and the value is its
        content.
    """

    ret = {}
    for filename in filenames:
        with open(filename, "r") as file:
            ret[filename] = json.load(file)
    return ret

####################
# Write file  
def write_file(filename, content, **kwargs) : 
    file = open(filename, mode="w", encoding="utf-8")
    ret = file.write(content)
    logger.info(f"... file {filename} has been already written.")
    file.close()
    return ret



############################################################
# function
def setup_root_logger(log_file):
    """
    Set up a root logger that logs messages to both a file and the console.

    Args:
    - `log_file` (str): The path to the log file.

    Returns:
    - A `logging.Logger` instance for the root logger.
    """
    # Set up the root logger with DEBUG level and two handlers: one that logs to a file, and one that logs to the console
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()],
        # Set the log message format
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-10s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
        )

    # Return the root logger instance
    return logging.getLogger()


# Get the logger object
logger = logging.getLogger(__name__)

############################################################
# function
def get_port_and_db(ssas_folder):
    """
    Get the port number and the database path for an SSAS instance.

    Parameters:
    ssas_folder (str): The path to the root folder of the SSAS instance.

    Returns:
    tuple: A tuple containing the port number (str) and the database path (str), or None if either or both values are not found.

    """

    # Log that the function is starting
    logger.info(f"Going to get port and database_id from path {ssas_folder}")
    
    # Define the name of the port file
    port_file_name = 'msmdsrv.port.txt'

    # Traverse the directory tree, looking for the port file and the database directory
    for root, dirs, files in os.walk(os.path.join(ssas_folder,'Data')):
        #pp(files)
        #pp(dirs)
        port = None
        db_id = None


        # get port
        if port_file_name in files:
            file_path = os.path.join(root, port_file_name)
            with open(file_path, 'r', encoding='utf-16-le') as f:
                port = f.read()
        
        # get db_id 

        for file_name in files:
            match = re.match(r'(.*)\.\d+\.db\.xml$', file_name)
            if match:
                db_id = match.group(1)
                break


        result = (port, db_id)
        break  

    # If no result was found, set it to None
    if 'result' not in locals():
        result = (None,None)
    else:
        # If a database directory was not found, return the port number and None for the database path
        if db_id is None:
            result = (port, None)

    logger.info(f"Connection to ssas is (localhost:{port}) and schema catalog name is: {db_id}")
    return(result)


############################################################
# function
def get_first_level_subfolders(folder_path):
    """
    Returns a list of first level subfolders in the given folder path.

    Args:
    folder_path (str): The path to the folder to search.

    Returns:
    list: A list of first level subfolders in the folder.
    """
    folder_path = os.path.expandvars(folder_path)

    logger.info(f"Getting a list of all items in the folder {folder_path}")
    # Get a list of all items in the folder
    #items = os.listdir(folder_path)

    # Filter the list to only include directories (subfolders)
    ret = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    
    logger.info(f"{len(ret)} folder(s) was found")

    return ret


import subprocess

############################################################
# function
def open_file_with_default_program(file_path):
    """
    Open the file located at the specified path using the default program associated with its file type.
    
    Args:
    file_path (str): The path of the file to be opened.

    Returns:
    None
    """
    time_in_seconds = 60
    logger.info(f"Try to open file {file_path}")
    subprocess.run(['start', '', file_path], shell=True)
    logger.info(f"Going to wait for {time_in_seconds} seconds.")
    time.sleep(time_in_seconds)

def open_file_with_default_program1(file_path):
    """
    Open the file located at the specified path using the default program associated with its file type.

    Args:
    file_path (str): The path of the file to be opened.

    Returns:
    int: PID of the process started to open the file.
    """
    time_in_seconds = 60
    absolute_path = os.path.abspath(file_path)
    print(f"Trying to open file {absolute_path}")
    
    process = subprocess.Popen(['start', 'PBIDesktopStore.exe', absolute_path], shell=True)
    pid = process.pid
    print(f"Process with PID {pid} started to open the file.")
    print(f"Waiting for {time_in_seconds} seconds...")
    time.sleep(time_in_seconds)
    return pid



############################################################
# function
def get_all_pbix_files(folder_path):
    """
    Returns a list of all .pbix files in the specified folder and its subfolders.

    Args:
        folder_path (str): The path to the folder to search for .pbix files.

    Returns:
        list: A list of absolute paths to all .pbix files found in the specified folder and its subfolders.
    """
    pbix_files = []  # Initialize an empty list to hold the paths of all .pbix files found

    logger.info(f"Getting pbix files from folder {folder_path}")
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.pbix'):  # Check if the file has a .pbix extension
                pbix_files.append(os.path.join(root, file_name))  # Add the absolute path of the .pbix file to the list

    logger.info(f"{len(pbix_files)} pbix file(s) was found")
    return pbix_files  # Return the list of .pbix files found




############################################################
# function
def camel(convertString: str) -> str:
    """
    Converts the given string to the CamelCase format.
    
    Arguments:
    convertString -- string to be converted to CamelCase format
    
    Returns:
    The resulting string in CamelCase format
    
    """

    # Replaces several different characters with spaces using a regular expression
    convertString = re.sub(r"(_|-|/|\+|~|!|@|#|\$|%|\^|&|\*|\(|\)|=|{|}|\[|\]|:|\"|;|\||,|\.|\<|\>|\?|\\)+"," ",convertString)
    
    # Converts each word in the string to the format with the first letter capitalized and the rest lowercase
    convertString = convertString.title().replace(" ","")
    
    # Removes spaces and converts the first letter of the string to uppercase
    convertedString = str(''.join([convertString[0].upper(),convertString[1:]]))
    
    # Returns the resulting string in CamelCase format
    return convertedString

############################################################
# function
def lower(convertString: str) -> str:
    """
    Converts the given string to lowercase.
    
    Arguments:
    convertString -- string to be converted to lowercase
    
    Returns:
    The resulting string in lowercase
    
    """

    # Converts the given string to lowercase
    convertedString = str(convertString).lower()
    
    # Returns the resulting string in lowercase
    return convertedString

############################################################
# function
import unicodedata

def convertCzech(convertString: str) -> str:
    """
    Converts the given Czech string to its ASCII equivalent.
    
    Arguments:
    convertString -- Czech string to be converted to ASCII
    
    Returns:
    The resulting string in ASCII format
    
    """
    
    # Normalizes the Czech string using NFD (Normalization Form D) to split accented characters into base and diacritic characters
    convertString = unicodedata.normalize('NFD', convertString)
    
    # Joins the base characters and removes the diacritic characters to convert the string to its ASCII equivalent
    convertedString = str(u"".join([c for c in convertString if not unicodedata.combining(c)]))
    
    # Returns the resulting string in ASCII format
    return convertedString

############################################################
# function
import zlib

def _cache_key_gen(sql: str, params: list = None) -> int:
        """
        Generates a cache key for the given SQL query and parameters.
        
        Arguments:
        sql -- SQL query to be cached
        params -- List of parameters to be passed to the SQL query (default None)
        
        Returns:
        A unique integer value (cache key) for the given SQL query and parameters
        
        """
        
        # Start with the SQL query
        cache_string = sql
        
        # If parameters are provided, add them to the cache string
        if params:
            cache_string = cache_string + '-'.join(map(str, params))
        
        # Convert the cache string to bytes using utf-8 encoding
        cache_string = bytes(cache_string, 'utf-8')
        
        # Calculate the 32-bit CRC (Cyclic Redundancy Check) value of the cache string
        cache_key = zlib.crc32(cache_string)
        
        # Return the cache key
        return cache_key


############################################################
# function
import os
import yaml

def save_df_to_yaml(df, file_name, dir_name):
    """
    Save pandas DataFrame to a YAML file with a given file name and directory name.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_name (str): The desired file name (including the .yaml extension).
        dir_name (str): The directory in which to save the YAML file.

    Returns:
        None
    """
    # Convert DataFrame to dictionary
    data_dict = df.to_dict()

    # Create directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Open file for writing
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as file:
        # Write dictionary to YAML file
        yaml.dump(data_dict, file)

    logger.info(f"Data saved to {file_path} successfully.")


############################################################
# function
import json

def save_df_to_json(df, file_name, dir_name):
    """
    Save pandas DataFrame to a JSON file with a given file name and directory name.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_name (str): The desired file name (including the .json extension).
        dir_name (str): The directory in which to save the JSON file.

    Returns:
        None
    """
    # Convert DataFrame to JSON string
    json_str = df.to_json(orient='records')

    # Convert JSON string to list of dictionaries
    data_dict = json.loads(json_str)

    # Create directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Open file for writing
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as file:
        # Write dictionary to JSON file
        json.dump(data_dict, file, indent=4)

    logger.info(f"Data saved to {file_path} successfully.")

############################################################
# function
def save_to_json(data, file_name, dir_name ):
    """
    TBD geb by chat gpt

    Parameters:

    Returns:
        None
    """
    # Create directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Open file for writing
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, 'w') as file:
        # Write dictionary to JSON file
        json.dump(data, file, indent=4)

    logger.info(f"Data saved to {file_path} successfully.")

############################################################
# function
import pandas as pd

def save_df_to_excel(df, file_name, dir_name):
    """
    Save pandas DataFrame to an Excel file with a given file name and directory name.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_name (str): The desired file name (including the .xlsx extension).
        dir_name (str): The directory in which to save the Excel file.

    Returns:
        None
    """
    # Create directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Construct file path
    file_path = os.path.join(dir_name, file_name)

    # Save DataFrame to Excel file
    with pd.ExcelWriter(file_path) as writer:
        df.to_excel(writer, index=False)

    logger.info(f"Data saved to {file_path} successfully.")

############################################################
# dconvert_timestamps_to_string
# ##############################
from pandas import Timestamp
def convert_timestamps_to_string(data):
    """
    Recursively traverses a data structure and converts any Timestamp objects to string representations.

    Args:
        data: The data structure (dictionary, list, or nested combination) to be processed.

    Returns:
        The processed data structure with Timestamp objects converted to string representations.

    """
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_timestamps_to_string(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = convert_timestamps_to_string(data[i])
    elif isinstance(data, Timestamp):
        data = data.isoformat()
    return data


############################################################
# df2listofdictsref
# ##############################
def df2listofdictsref(df):
    ''' convert pandas.DataFrame to list of dicts records
    
    Args:
        df - pandas.DataFrame
    
    Returns:
        ret - pointer to array of dict
        example 
        [
            {'TABLE_NAME': 'testcase', 'TABLE_SCHEMA': 'datamart', 'TABLE_CATALOG': 'sqa_datamart', 'TABLE_TYPE': 'BASE TABLE'},
            {'TABLE_NAME': 'testsuite', 'TABLE_SCHEMA': 'datamart', 'TABLE_CATALOG': 'sqa_datamart', 'TABLE_TYPE': 'BASE TABLE'}
        ]
    '''
    ret = df.to_dict('records')
    logger.info("Convert pandas.DataFrame to ref array of dict")
    #print(type(ret))
    return ret

############################################################
# df2dictofdictsref
# ##############################
def df2dictofdictsref(df, idx):
    ''' convert pandas.DataFrame dicts of dicts 
    
    Args:
        df - pandas.DataFrame
        idx - unique key for each record
    
    Returns:
        ret - pointer to dict of dict
        example 
        {
            'testcase': {'TABLE_NAME': 'testcase', 'TABLE_SCHEMA': 'datamart', 'TABLE_CATALOG': 'sqa_datamart', 'TABLE_TYPE': 'BASE TABLE'},
            'testsuite': {'TABLE_NAME': 'testsuite', 'TABLE_SCHEMA': 'datamart', 'TABLE_CATALOG': 'sqa_datamart', 'TABLE_TYPE': 'BASE TABLE'}
        }
    '''
    logger.info("Convert pandas.DataFrame to ref dict of dict")
    
    # verify uniquity  of index, convert index column to series and test uniquity 
    # https://datatofish.com/pandas-dataframe-to-series/
    
    # squeeze sotime retuns string object and this situation must be managed 
    #if not type(df[idx].squeeze()) == str and not df[idx].squeeze().is_unique : 
    #    self.logger.info("name of IDX"+ idx)
    #    raise Exception("IDX is not unique. Be aware it is case sensitive")

    # convert  
    ret = df.set_index(idx, drop=False, verify_integrity=True).to_dict('index') #verify_integrity check duplicities 
    #print(type(ret))
    #print(ret)
    return ret


def get_short_git_hash():
    """
    Retrieves the short hash of the current Git commit.

    Returns:
        str or None: The short Git hash as a string, or None if the Git command fails.
    """
    try:
        # Execute the Git command to retrieve the short hash of the current commit.
        git_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        # If the Git command fails, return None.
        git_hash = None
    # Return the short Git hash as a string.
    return git_hash



from jinja2 import Environment, FileSystemLoader

def init_templ_env(template_dir):
    """
    Initializes a Jinja2 environment with templates from the specified directory.

    Args:
        template_dir (str): The directory containing the Jinja2 templates.

    Returns:
        jinja2.Environment: A Jinja2 environment object configured to load templates from the specified directory.
    """
    logger.info(f"Init folder {template_dir} as Jinja2 env folder.")
    
    # Create a Jinja2 environment object that loads templates from the specified directory.
    env = Environment(
        loader=FileSystemLoader(template_dir),
        extensions=['jinja2_time.TimeExtension']
        )
    
    # Return the environment object.
    return env


def get_pbix_filename_from_trc(file):
    """
    Extracts the name of the PBIX file from the FlightRecorderCurrent.trc file.
    
    Args:
        file (str): The path to the FlightRecorderCurrent.trc file.
    
    Returns:
        str: The name of the PBIX file, including its full path.
    """
    pbix_filename = ''
    
    logger.info(f"Try to find pbix file name in file {file}.")
    # Open the TRC file in read mode with utf-16le encoding, ignoring decoding errors
    with open(file, encoding='utf-16le', errors='ignore') as f:
        # Read the contents of the file and store them in a list of lines
        content = f.readlines()
        
        # Iterate over the lines in the file
        for line in content:
            # Check if the line contains the 'ddl700_700:PackagePath' string
            if 'ddl700_700:PackagePath' in line:
                # Use regular expressions to extract the value between the <ddl700_700:PackagePath> tags
                match = re.search(r'<ddl700_700:PackagePath>(.*?)</ddl700_700:PackagePath>', line)
                
                # If a match is found, set the pbix_filename variable to the extracted value
                if match:
                    pbix_filename = match.group(1)
    
    logger.info(f"Pbix path is {pbix_filename}.")
    
    # Return the name of the PBIX file
    return pbix_filename

##############################
# cat long string and add this lenght at end
def str_slicer(text, num=20):
    if len(text) > num:
        ret = "%s..(%s)" % (text[:num],len(text))  
    else:
        ret = text
    return ret

##############################
# remove -nan- string 
def remove_nan(text,replace = 'n/a'):
    if text == '-NaN-':
        ret = replace  
    else:
        ret = text
    return ret
