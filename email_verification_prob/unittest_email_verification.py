import unittest
from email_verification_prob.function import *


class MyTestCase(unittest.TestCase):
    def test_case(self):
        valid_email = "bebegam@outlook.com"
        self.assertTrue(validate_email(valid_email))

    def test_case1(self):
        valid_email = "emailisbena@gmail.com"
        self.assertTrue(validate_email(valid_email))

if __name__ == '__main__':
    unittest.main()