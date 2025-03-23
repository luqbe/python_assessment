import unittest
from text_alignment.function import*


class testcase(unittest.TestCase):
      def test_1(self):
          thickness = int(input("Enter thickness an odd number: "))
          expected_output = txt_align(thickness, c="H")
          actual_output = [
              '  H  ',
              ' HHH ',
              'HHHHH',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              ' HHHHHHHHHHHHHHH  ',
              ' HHHHHHHHHHHHHHH  ',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              ' HHH         HHH        ',
              '            HHHHH ',
              '             HHH  ',
              '              H   ',
          ]

          self.assertEqual(expected_output,expected_output)


if __name__ == '__main__':
    unittest.main()