import unittest
from meanvar_problem.function import*

class testcase(unittest.TestCase):
      def test_case(self):
          actual_input=mean_var_stud([[3,4,5],[5,6,7],[3,4,5]])
          expected_output="[4. 6. 4.]\n[0.88888889 0.88888889 0.88888889]\n1.24721912892"
          self.assertEqual(actual_input,expected_output)




if __name__ == '__main__':
    unittest.main()