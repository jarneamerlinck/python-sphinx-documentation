import unittest
import pytest
from packagename_jarne.PID import PID

class TestPID(unittest.TestCase):
	def test_create_PID_object(self):
		
		self.pid = PID()
		self.assertEqual(self.pid.Kp , 0, "Should be 0")
		self.assertEqual(self.pid.Kd , 0, "Should be 0")
		self.assertEqual(self.pid.Ki , 0, "Should be 0")
		self.assertEqual(self.pid.prev_error , 0, "Should be 0")
		self.assertEqual(self.pid.Cp , 0, "Should be 0")
		self.assertEqual(self.pid.Ci , 0, "Should be 0")
		self.assertEqual(self.pid.Cd , 0, "Should be 0")
		