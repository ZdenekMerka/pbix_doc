##############################
# How to run 
# python -m unittest discover tests/ -vvv

import unittest
import os
import sys
from pprint import pprint as pp

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import lib.tools as tools

##############################
# 
class test_tools(unittest.TestCase):
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

