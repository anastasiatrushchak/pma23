import unittest
from ComplexNumber import ComplexNumber

class Test_ComplexNumber(unittest.TestCase):

    def test_conjugate(self):
        complex = ComplexNumber(12,2)
        self.assertEqual(complex.conjugate(),  ComplexNumber(12, -2))
    def test_abs(self):
        complex = ComplexNumber(6,-8)
        self.assertEqual(abs(complex),  ComplexNumber(10, 0))

    def test_str_representation(self):
        complex = ComplexNumber(2, -3)
        self.assertEqual(str(complex), "(2-3j)")

    def test_equality(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(2, 3)
        num3 = ComplexNumber(4, 5)

        self.assertEqual(num1, num2)
        self.assertNotEqual(num1, num3)

    def test_addition(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(4, 5)

        self.assertEqual(num1 + num2, ComplexNumber(6, 8))

    def test_subtraction(self):
        num1 = ComplexNumber(4, 5)
        num2 = ComplexNumber(2, 3)
        self.assertEqual(num1 - num2, ComplexNumber(2,2))

    def test_multiplication(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(4, 5)
        prod_result = num1 * num2
        self.assertEqual(num1 * num2, ComplexNumber(-7, 22))

    def test_division(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(4, 5)
        div_result = num1 / num2
        self.assertAlmostEqual(div_result.real, 0.5609756097560976)
        self.assertAlmostEqual(div_result.imag, 0.0487804878048781)

if __name__ == '__main__':
    unittest.main()