import unittest
import hungarian as hun
import numpy as np

class TestHungarian(unittest.TestCase):

    def test_unsolved(self):
        state = hun.HungarianAlg(np.asarray([[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]))

        self.assertRaises(Exception)

    def test_square_matrix(self):
        state = hun.HungarianAlg(np.asarray([[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]))
        state.solve()

        self.assertEqual(state.minimum_cost,140)

    def test_retangular_matrix(self):
        state = hun.HungarianAlg(np.asarray([[5,51],[445,2],[551,23],[415,566]]))
        state.solve()

        self.assertEqual(state.minimum_cost,7)

    def test_retangular_matrix_with_tie(self):
        state = hun.HungarianAlg(np.asarray([[5,51],[5,10],[551,23],[415,566]]))
        state.solve()

        self.assertEqual(state.minimum_cost,15)

    def test_zero_cost_matrix(self):
        state = hun.HungarianAlg(np.asarray([[0,0],[0,0],[0,0],[0,0]]))
        state.solve()

        self.assertEqual(state.minimum_cost,0)

if __name__ == '__main__':
    unittest.main()