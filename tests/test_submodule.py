import unittest
import packagename_jarne.submodule

class TestImport(unittest.TestCase):

	def test_creation_of_object_base(self):
		"""Test submodule import.
		"""  
		from packagename_jarne.submodule.base import Base
		string = "text"
		number=3
		obj = Base(string)
		result = obj.run(number)
		self.assertEqual(obj.text, "_text3")
		self.assertEqual(obj.text, f"_{result}")

	def test_creation_of_object_extended(self):
		"""Test ExtendedClass.
		"""  
		from packagename_jarne.submodule.extended import ExtendedClass

		string = "text"
		number=3
		obj = ExtendedClass(string)
		result = obj.run(number)
		self.assertEqual(obj.text, "_texttexttext")
		self.assertEqual(obj.text, f"_{result}")
	
	def test_creation_of_object_extended2(self):
		"""Test Extended2Class.
		"""  
		from packagename_jarne.submodule.extended import Extended2Class

		string = "text"
		number=3
		obj = Extended2Class(string)
		result = obj.run(number)
		self.assertEqual(obj.text, "_text3")
		self.assertEqual(result, "not")
	