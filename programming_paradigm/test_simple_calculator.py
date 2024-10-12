import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-8, 1), -9)
        
        
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
                
        
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 10), 1)
        self.assertEqual(self.calc.divide(-4, 4), -1)
        self.assertRaises (ZeroDivisionError, self.calc.divide, 10, 0)
if __name__ == '__main__':
    unittest.main()


