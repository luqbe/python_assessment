import unittest
from word_order_problem.function import*

class testcase(unittest.TestCase):
      def test_1(self):
          actual_input=word_order(5,['roses', 'rosemary', 'roses', 'rosemary', 'rosam'])
          expected_output=(3, [2, 2, 1])
          self.assertEqual(actual_input,expected_output)


if __name__ == '__main__':
    unittest.main()