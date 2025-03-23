import unittest
from namedtuple.function import *

class testcase(unittest.TestCase):
      def test_1(self):
          students_data = [
              "5",
              "ID MARKS NAME CLASS",
              "1 91 john 7",
              "2 75 Peter 4",
              "3 76 Kelvin 9",
              "4 98 Elin 5",
              "5 89 Elizabeth 6"
          ]
          given_output=calculate_average_mark(students_data)
          expected_output=85.80
          self.assertEqual(float(given_output), float(expected_output))


if __name__ == '__main__':
    unittest.main()
