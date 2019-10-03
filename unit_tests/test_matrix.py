import sys
sys.path.insert(1, '../')
from matrix import Matrix
import unittest

class MatrixTest(unittest.TestCase):
    def test_matrix_multiplication(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[1, 2], [3, 4], [5, 6]])
        m_expect = Matrix([[22, 28], [49, 64]])
        self.assertEqual(m_expect, m1 * m2)

        m1 = Matrix([[-1, -2, -3], [-4, -5, -6]])
        m2 = Matrix([[1, 2], [3, 4], [5, 6]])
        m_expect = Matrix([[-22, -28], [-49, -64]])
        self.assertEqual(m_expect, m1 * m2)

    def test_scalar_multiplication(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        s = 10
        m_expect = Matrix([[10, 20, 30], [40, 50, 60]])
        self.assertEqual(m_expect, m * s)
        self.assertEqual(m_expect, s * m)
    
    def test_copy(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = m1.copy()
        self.assertEqual(m1, m2)
    
    def test_zero_matrix(self):
        m = Matrix.zero_matrix(2, 3)
        m_expect = Matrix([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(m_expect, m)

    def test_apply_function(self):
        f = lambda x: x * x
        m = Matrix([[1, 2], [3, 4]])
        m = m.apply_function(f)
        m_expect = Matrix([[1, 4], [9, 16]])
        self.assertEqual(m_expect, m)
    
    def test_add(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 1], [2, 2]])
        m_expect = Matrix([[2, 3], [5, 6]])
        self.assertEqual(m_expect, m1 + m2)
