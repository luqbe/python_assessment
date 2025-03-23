import unittest
from iterators_problem.function import*

class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = probability_of_a(4, "aacd", 2)
        expected_output = 0.8333333
        self.assertEqual(actual_input, expected_output)

    def test_case1(self):
        actual_output = probability_of_a(5, "aaeed", 2)
        expected_output = 0.7
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

