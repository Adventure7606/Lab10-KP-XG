#https://github.com/Adventure7606/Lab10-KP-XG.git
import unittest

from calculator import *
class TestCalculator(unittest.TestCase):
    def test_add(self):
         self.assertEqual(add(1,2),3)
         self.assertEqual(add(5,4), 9)
         self.assertEqual(add(-5,4),-1)
    def test_subtract(self):
         self.assertEqual(subtract(15,3),12)
         self.assertEqual(subtract(2,3),-1)
         self.assertEqual(subtract(7,4),3)
    def test_multiply(self): # 3 assertions
         self.assertEqual(mul(5,3), 15)
         self.assertEqual(mul(-7, 3), -21)
         self.assertEqual(mul(-8, -8), 64)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1,3),3)
        self.assertEqual(div(5, 25), 5)
        self.assertEqual(div(-1, 5), -5)


    def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                (div(0,5),9)



    def test_logarithm(self):
        self.assertEqual(logarithm(8,8),1)
        self.assertEqual(logarithm(5,5),1)
        self.assertEqual(logarithm(2,2),1)



    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            (logarithm(0,  1), -2)


    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(9, 12), 15)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(144), 12)
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()