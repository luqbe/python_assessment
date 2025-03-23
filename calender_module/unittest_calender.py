
import unittest
from calender_module.calender import *

class calender(unittest.TestCase):
     def test_1(self):
         actual_input=find_day("08 06 2015")
         expected_output="Thursday"
         self.assertEqual(actual_input,expected_output)


if __name__ == '__main__':
    unittest.main()
