import unittest
from mutation_prog.funtion import *

class testcase(unittest.TestCase):
      def test_1(self):
          given_input=mutation("welcome",3,"n")
          expected_output= "welnome"
          self.assertEqual(given_input, expected_output)

if __name__ == '__main__':
  unittest.main()

