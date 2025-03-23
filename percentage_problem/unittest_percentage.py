import unittest
from percentage_problem.function import*

class testcase(unittest.TestCase):
      def test_1(self):
          actual_input=average_cal({'John': [70, 80, 20],'peter':[90,78,85],'kevin':[88,67,95]},'John')
          expected_output=56.67
          self.assertEqual(float(actual_input),float(expected_output))


if __name__ == '__main__':
    unittest.main()
