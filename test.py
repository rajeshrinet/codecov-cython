import matMul
import numpy as np
import unittest

class  ExTest(unittest.TestCase):
    def test_multiply(self):
        A = np.array((1, 2, 300, 400, 400))
        B = np.array((1, 2, 3, 4, 5))
        
        diff = A*B - matMul.multiply(A, B)
        self.assertTrue((np.asarray(diff) < 0.001).all(),
                           "Multiplication is not correct")

    def test_divide(self):
        A = np.array((1, 2, 300, 400, 400))
        B = np.array((1, 2, 3, 4, 5))
        
        diff = A*B - matMul.multiply(A, B)
        self.assertTrue((np.asarray(diff) < 0.001).all(),
                           "Multiplication is not correct")

if __name__ == '__main__':
    unittest.main()
