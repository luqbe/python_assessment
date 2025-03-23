import unittest
from min_max_problem.function import*

class testcase(unittest.TestCase):
      def test_1(self):

          actual_output=min_max_2d([[4, 3], [8, 7], [2, 7], [6, 2], [4, 1]])
          expected_output=7
          self.assertEqual(actual_output,expected_output)



if __name__ == '__main__':
    unittest.main()

