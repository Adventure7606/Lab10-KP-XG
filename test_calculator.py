import unittest
from calculator import add,sub,div,log,exp

class TestCalculator(unittest.TestCase):
    ######### Partner 2
     def test_add(self):
         self.assertEqual(add(1,2),3)
         self.assertEqual(add(5,4), 9)
         self.assertEqual(add(-5,4),-1)



     def test_subtract(self):
         self.assertEqual(sub(15,3),12)
         self.assertEqual(sub(2,3),-1)
         self.assertEqual(sub(7,4),3)



    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
     def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                (div(0,5),9)



     def test_logarithm(self):
        self.assertEqual(log(8,8),1)
        self.assertEqual(log(5,5),1)
        self.assertEqual(log(2,2),1)



     def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            (log(0,  1), -2)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()