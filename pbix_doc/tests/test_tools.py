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

##############################
# 
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


from lib.tools import get_first_level_subfolders

class TestGetFirstLevelSubfolders(unittest.TestCase):
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

import subprocess
from unittest.mock import patch

from lib.tools import open_file_with_default_program

class TestOpenFileWithDefaultProgram(unittest.TestCase):
    @patch('subprocess.run')
    def test_file_opened_with_default_program(self, mock_subprocess):
        file_path = os.path.join(os.getcwd(), 'test_file.txt')
        open_file_with_default_program(file_path)
        mock_subprocess.assert_called_once_with(['start', '', file_path], shell=True)

from tempfile import TemporaryDirectory
from lib.tools import get_all_pbix_files

class TestGetAllPbixFiles(unittest.TestCase):

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


