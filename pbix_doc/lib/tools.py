from pprint import pprint as pp
import os
import logging
import time
import re

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
        result = None
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
    logger.info(f"Try to open file {file_path}")
    subprocess.run(['start', '', file_path], shell=True)
    logger.info(f"Going to wait for 1 minutes.")
    time.sleep(60)




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
