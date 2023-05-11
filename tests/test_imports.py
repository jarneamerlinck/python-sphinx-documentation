import unittest

class TestImport(unittest.TestCase):
	def test_base_import(self):
		"""Test base import.
		"""    
		import packagename_jarne
	def test_datasets_import(self):
		"""Test submodule import.
		"""  
		import packagename_jarne.submodule
	def test_functions_import(self):
		"""Test functions import.
		"""  
		import packagename_jarne.functions