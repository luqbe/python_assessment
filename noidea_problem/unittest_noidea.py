import unittest
from noidea_problem.function import *
from noidea_problem.input import n


class testcase(unittest.TestCase):
      def test_1(self):
          n, m = 4, 3
          arr = [1, 2, 3, 4]
          A = [1, 3]
          B = [2,4]
          actual_input=calculate_happiness(n,m,arr,A,B)
          expected_output=0
          self.assertEqual(actual_input,expected_output)




if __name__ == '__main__':
    unittest.main()

