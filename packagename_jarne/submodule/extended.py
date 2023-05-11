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


from packagename_jarne.submodule.base import *

# Create extended class for Base
class ExtendedClass(Base): 
	def __init__(self, text:str):

		self.text = text

	def run(self)-> str:
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
		self.text = self.text * number
  
class Extended2Class(Base): 
	def __init__(self, text:str):

		self.text = text

	def run(self)-> str:
		"""Run method.

		Returns:
			str: Returns string.
		"""		
		return "not"