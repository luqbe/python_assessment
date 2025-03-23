import unittest
from linearalgebra.function import *

class mytestcase(unittest.TestCase):
      def test_case(self):
          actual_input=determinant([[2,3],[4,5]])
          expected_output=-2.0
          self.assertequal=(actual_input,expected_output)

if __name__ == '__main__':
    unittest.main()