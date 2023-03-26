##############################
# How to run 
# python -m unittest discover tests/ -vvv

import unittest
import os
import sys
from pprint import pprint as pp

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import lib.conf as cnf

##############################
# 
class test_conf(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.conf = cnf.get_conf('conf/common.yaml')
        #pp(self.conf)
    
    def test_01_conf_default(self):
        ret = self.conf
        self.assertEqual(ret['db_connection_file'],'conf\\connections.yaml', " Test Get conf db_connection_file")
    
    def test_02_conf_default(self):
        ret = self.conf
        #pp(ret)
        self.assertEqual(ret['output_folder']['path'],'.\output', " Test Get conf 2")
    
    def test_03_conf_default(self):
        ret = self.conf
        pp(sorted(list(ret.keys())))
        self.assertEqual(sorted(list(ret.keys())), sorted([
            'connection_file',
            'local_ssas_folder',
            'log_file',
            'output_folder',
            'project_description',
            'project_name',
            'select_top',
            'template_folder'
        ]), " Test Get conf 3 keys")
    
    def test_04_get_conf_empty(self):
        with self.assertRaises(TypeError) as context:
            cnf.get_connections()
        self.assertEqual(str(context.exception), "expected str, bytes or os.PathLike object, not NoneType")
