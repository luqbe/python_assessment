import unittest
from piling_up.function import*


class testcase(unittest.TestCase):
      def test_1(self):
          actual_input=piling_up(1,[[4, 3, 2, 2, 2, 4]])
          expected_output='Yes'
          self.assertEqual(actual_input,expected_output)


if __name__ == '__main__':
    unittest.main()