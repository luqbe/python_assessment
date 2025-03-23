import unittest
from runnerup_score.function import *


class testcase(unittest.TestCase):
      def test_1(self):
          actual_input=runner_up([67,78,69])
          exp_output= 69
          self.assertEqual(actual_input,exp_output)

if __name__ == '__main__':
    unittest.main()