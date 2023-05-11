import unittest
from packagename_jarne.PID import PID

class TestPID(unittest.TestCase):
	def test_create_PID_object(self):
		"""Test create PID object.
		"""		
		pid = PID()
		self.assertEqual(pid.Kp , 0, "Should be 0")
		self.assertEqual(pid.Kd , 0, "Should be 0")
		self.assertEqual(pid.Ki , 0, "Should be 0")
		self.assertEqual(pid.prev_error , 0, "Should be 0")
		self.assertEqual(pid.Cp , 0, "Should be 0")
		self.assertEqual(pid.Ci , 0, "Should be 0")
		self.assertEqual(pid.Cd , 0, "Should be 0")
		