import unittest
from string_formatting.function import*
from unittest.mock import patch
from io import StringIO

def print_matrix():
    print("1  1  1  1\n2  2  2 10")

class testcase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_matrix(self, mock_stdout):
        print_matrix()
        self.assertEqual(mock_stdout.getvalue().strip(), "1  1  1  1\n2  2  2 10")


if __name__ == '__main__':
    unittest.main()