##############################
# How to run 
# python -m unittest discover tests/ -vvv

import unittest
import os
import sys
import tempfile
from pprint import pprint as pp

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import lib.tools as tools

############################################################
class test_01_tools(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log_file = 'example.log'
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_01_logger_output(self):
        import logging 
        logger = tools.setup_logger(self.log_file)

        # Check that the log file was created
        self.assertTrue(os.path.exists(self.log_file))

        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        
        
        # Check that the log file contains the expected messages
        with open(self.log_file) as f:
            log_contents = f.read()
        self.assertIn('This is a debug message', log_contents, 'Debug message')
        self.assertIn('This is an info message', log_contents, 'Info message')
        self.assertIn('This is a warning message', log_contents, 'Warning message')

        # Check that the logger is set up correctly
        self.assertEqual(logger.level, logging.DEBUG)
        self.assertEqual(len(logger.handlers), 2)


############################################################
from lib.tools import get_port_and_db

class Test02GetPortAndDb(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Create a temporary directory for testing and write a port file
        self.temp_dir = 'temp_test_dir'
        self.port_file = 'msmdsrv.port.txt' 
        self.db_id_file = 'test_214c4853-f9f3-4f9c-a4dd-69c257a86419.0.db'
        os.mkdir(self.temp_dir)
        with open(os.path.join(self.temp_dir, self.port_file), 'w') as f:
            f.write('12345')
        # Create a subdirectory with suffix '0.db'
        os.mkdir(os.path.join(self.temp_dir, self.db_id_file))

    @classmethod
    def tearDownClass(self):
        # Remove the temporary directory after testing
        port_file_path = os.path.join(self.temp_dir, self.port_file)
        db_id_file_path = os.path.join(self.temp_dir, self.db_id_file)

        # delete file if exits
        if os.path.exists(port_file_path):
            os.remove(port_file_path)

        # delete foleder if exits
        if os.path.exists(db_id_file_path) and os.path.isdir(db_id_file_path):
            os.rmdir(db_id_file_path)
        
        os.rmdir(self.temp_dir)

    def test_02_get_port_and_db(self):
        # Test if the function returns the correct port and directory paths
        expected_result = ('12345', os.path.join(self.temp_dir, self.db_id_file))
        actual_result = get_port_and_db(self.temp_dir)

        self.assertEqual(actual_result, expected_result)

    def test_03_get_port_and_db_no_db(self):
        # Test if the function returns None for the db path if no directory with suffix '0.db' is found
        os.rmdir(os.path.join(self.temp_dir, self.db_id_file))
        expected_result = ('12345', None)
        actual_result = get_port_and_db(self.temp_dir)
        self.assertEqual(actual_result, expected_result)

    def test_04_get_port_and_db_no_port(self):
        # Test if the function returns None if no port file is found
        os.remove(os.path.join(self.temp_dir, self.port_file))
        expected_result = (None,None)
        actual_result = get_port_and_db(self.temp_dir)
        self.assertEqual(actual_result, expected_result)


############################################################
from lib.tools import get_first_level_subfolders

class Test03GetFirstLevelSubfolders(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # Create a temporary directory with some subfolders for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        os.mkdir(os.path.join(self.temp_dir.name, 'subfolder1'))
        os.mkdir(os.path.join(self.temp_dir.name, 'subfolder2'))
        os.mkdir(os.path.join(self.temp_dir.name, 'subfolder2', 'subfolder22'))
        #os.mkdir(os.path.join(self.temp_dir.name, 'file1.txt'))
        open(os.path.join(self.temp_dir.name, 'file1.txt'), mode='w').close()
        #dir_list = os.listdir(self.temp_dir.name)
        #pp(dir_list)

    @classmethod
    def tearDownClass(self):
        # Clean up the temporary directory after testing
        self.temp_dir.cleanup()

    def test_get_first_level_subfolders(self):
        # Test that the function returns the correct list of subfolders
        subfolders = get_first_level_subfolders(self.temp_dir.name)
        #pp(subfolders)
        self.assertCountEqual(subfolders, ['subfolder1', 'subfolder2'])
    
    def test_get_first_level_subfolders2(self):
        # Test that the function returns the correct list of subfolders
        second_level = os.path.join(self.temp_dir.name, 'subfolder2')
        subfolders = get_first_level_subfolders(second_level)
        #pp(subfolders)
        self.assertCountEqual(subfolders, ['subfolder22'])

##############################
import subprocess
from unittest.mock import patch

from lib.tools import open_file_with_default_program

class Test04OpenFileWithDefaultProgram(unittest.TestCase):
    @patch('subprocess.run')
    def test_file_opened_with_default_program(self, mock_subprocess):
        file_path = os.path.join(os.getcwd(), 'test_file.txt')
        open_file_with_default_program(file_path)
        mock_subprocess.assert_called_once_with(['start', '', file_path], shell=True)

##############################
from tempfile import TemporaryDirectory
from lib.tools import get_all_pbix_files
class Test05GetAllPbixFiles(unittest.TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.temp_subdir = os.path.join(self.temp_dir.name, 'subdir')
        os.makedirs(self.temp_subdir)

        # Create sample files with different extensions
        with open(os.path.join(self.temp_dir.name, 'file1.pbix'), 'w') as f:
            f.write('sample content')
        with open(os.path.join(self.temp_subdir, 'file2.txt'), 'w') as f:
            f.write('sample content')
        with open(os.path.join(self.temp_dir.name, 'file3.pbix'), 'w') as f:
            f.write('sample content')
        with open(os.path.join(self.temp_subdir, 'file4.pbix'), 'w') as f:
            f.write('sample content')
        with open(os.path.join(self.temp_subdir, 'file5.pbix.backup'), 'w') as f:
            f.write('sample content')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_get_all_pbix_files(self):
        pbix_files = get_all_pbix_files(self.temp_dir.name)
        expected_files = [os.path.join(self.temp_dir.name, 'file1.pbix'),
                          os.path.join(self.temp_dir.name, 'file3.pbix'),
                          os.path.join(self.temp_subdir, 'file4.pbix')]
        self.assertEqual(pbix_files, expected_files)

##############################
from lib.tools import camel
class TestCamel(unittest.TestCase):
    
    def test_camel(self):
        self.assertEqual(camel('Příliš žluťoučký kůň úpěl ďábelské ódy.'),'PřílišŽluťoučkýKůňÚpělĎábelskéÓdy',"Test function camel")
        self.assertEqual(camel("my_variable_name"), "MyVariableName")
        self.assertEqual(camel("this-is-a-test"), "ThisIsATest")
        self.assertEqual(camel("a_long/path/to+a_file.txt"), "ALongPathToAFileTxt")
        self.assertEqual(camel("12345"), "12345")


############################################################
from lib.tools import lower

class TestLower(unittest.TestCase):
    
    def test_lower(self):
        self.assertEqual(lower("MY STRING"), "my string")
        self.assertEqual(lower("HeLLo WoRLd"), "hello world")
        self.assertEqual(lower(""), "")
        self.assertEqual(lower("12345"), "12345")



############################################################
from lib.tools import convertCzech
class TestConvertCzech(unittest.TestCase):
    
    def test_convertCzech(self):
        self.assertEqual(convertCzech("žluťoučký kůň"), "zlutoucky kun")
        self.assertEqual(convertCzech("Příliš žluťoučký kůň úpěl ďábelské ódy."), "Prilis zlutoucky kun upel dabelske ody.")
        self.assertEqual(convertCzech("Když jsem byl malý, říkali mi Pepíček."), "Kdyz jsem byl maly, rikali mi Pepicek.")
        self.assertEqual(convertCzech("časopis Život"), "casopis Zivot")


############################################################
from lib.tools import _cache_key_gen
class TestCacheKeyGen(unittest.TestCase):
    
    def test_cache_key_gen(self):
        sql = "SELECT * FROM users WHERE username = ? AND age > ?"
        params = ["john", 25]
        expected_output = 3436099716
        self.assertEqual(_cache_key_gen(sql, params), expected_output)
        
        sql = "SELECT * FROM posts WHERE category = ? AND published = ?"
        params = ["news", True]
        expected_output = 566373666
        self.assertEqual(_cache_key_gen(sql, params), expected_output)
        
        sql = "SELECT COUNT(*) FROM comments WHERE post_id = ?"
        params = [10]
        expected_output = 29295974
        self.assertEqual(_cache_key_gen(sql, params), expected_output)

############################################################
import os
import yaml
import pandas as pd
from lib.tools import save_df_to_yaml

class TestSaveDfToYaml(unittest.TestCase):
    def setUp(self):
        self.data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
        self.df = pd.DataFrame(self.data)

    def test_save_df_to_yaml(self):
        dir_name = 'test_data'
        file_name = 'test.yaml'
        save_df_to_yaml(self.df, file_name, dir_name)

        file_path = os.path.join(dir_name, file_name)
        with open(file_path, 'r') as file:
            loaded_dict = yaml.safe_load(file)

        self.assertEqual(loaded_dict, {'Age': {0: 25, 1: 30, 2: 35}, 'Name': {0: 'Alice', 1: 'Bob', 2: 'Charlie'}} , 'Test 01')
        self.assertTrue(os.path.exists(file_path), 'Test 02')

    def tearDown(self):
        dir_name = 'test_data'
        file_name = 'test.yaml'
        file_path = os.path.join(dir_name, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(dir_name):
            os.rmdir(dir_name)

############################################################
import json
from lib.tools import save_df_to_json

class TestSaveDfToJson(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
        self.dir_name = 'test_dir'
        self.file_name = 'test.json'
        
    def test_save_df_to_json(self):
        # Save the DataFrame to a JSON file
        save_df_to_json(self.df, self.file_name, self.dir_name)
        
        # Check that the file was created
        file_path = os.path.join(self.dir_name, self.file_name)
        self.assertTrue(os.path.exists(file_path))
        
        # Read the JSON file and check that its contents are correct
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{'col1': 1, 'col2': 'a'}, {'col1': 2, 'col2': 'b'}, {'col1': 3, 'col2': 'c'}])
        
    def tearDown(self):
        # Remove the test directory and its contents
        test_dir = os.path.join(os.getcwd(), self.dir_name)
        if os.path.exists(test_dir):
            for file in os.listdir(test_dir):
                os.remove(os.path.join(test_dir, file))
            os.rmdir(test_dir)

############################################################
import json
from lib.tools import save_df_to_excel

class TestSaveDfToExcel(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        self.file_name = 'test.xlsx'
        self.dir_name = 'test_dir'
        
    def tearDown(self):
        file_path = os.path.join(self.dir_name, self.file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(self.dir_name):
            os.rmdir(self.dir_name)
    
    def test_save_df_to_excel(self):
        save_df_to_excel(self.df, self.file_name, self.dir_name)
        file_path = os.path.join(self.dir_name, self.file_name)
        self.assertTrue(os.path.exists(file_path))
        loaded_df = pd.read_excel(file_path)
        pd.testing.assert_frame_equal(self.df, loaded_df)
        
