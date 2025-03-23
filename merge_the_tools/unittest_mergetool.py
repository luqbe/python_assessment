import unittest
from merge_the_tools.function import*

class mytestcase(unittest.TestCase):
      def test_1(self):
          actual_input=(merge_the_tools("AACBBDHJK",3))
          expected_output="AC\nBD\nHJK"
          self.assertEqual(actual_input,expected_output)


if __name__ == '__main__':
    unittest.main()