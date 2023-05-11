"""Module with the parent classes for the example. Needs to be implemented to use.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from packagename_jarne.submodule.base import *

	# Create extended class for Base
	class ExtendedClass(Base): 
		def __init__(self, text:str):
	
			self.text = text

		def run(self):
			print(self.text)
	ext_obj = ExtendedClass("text")
	ext_obj.run(3)

"""


from typing_extensions import override


class MetaBase(type):
	"""Meta class for Base.

	changes input for run.
	"""	
	@staticmethod
	def wrap(func):
		"""Return a wrapped instance method"""
		def outer(self, number):
			# print("Create Temp")
			self.convert_string(number)
			return_value = func(self)
			self.text = "_" + self.text
			# print( "Remove Temp")
			return return_value
		return outer

	def __new__(cls, name, bases, attrs):
		"""If the class has a method in TO_CHANGE, wrap it"""

		method_name:str = "run"

		if method_name in attrs:
			attrs[method_name] = cls.wrap(attrs[method_name])
		return super(MetaBase, cls).__new__(cls, name, bases, attrs)


class Base(metaclass=MetaBase):
	"""Example base class.
	"""    
	def __init__(self, text:str):
		"""Example base class.

		Args:
			text (str): Text.
		"""     
		self.text:str = text

	@override
	def run(self) -> str:
		"""Run method.

		Returns:
			str: Returns string.
		"""		 
		return self.text

	def convert_string(self, number:int):
		"""converts string by number.

		Args:
			number (int): number.
		"""     
		self.text = self.text + str(number)