import unittest
from timedelta.function import*

class testcase(unittest.TestCase):
      def test_1(self):
          actual_input=time_difference("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
          expected_output=25200.0
          self.assertEqual(float(actual_input),float(expected_output))


if __name__ == '__main__':
    unittest.main()
