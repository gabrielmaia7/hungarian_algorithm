import unittest
import hungarian as hun
import numpy as np

class TestHungarian(unittest.TestCase):

    def test_square_matrix(self):
        state = hun.HungarianAlg(np.asarray([[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]))
        step = state.initial_step
    
        while type(step) is not tuple:
            step = step(state)

        self.assertEqual(step[1],140)

    def test_retangular_matrix(self):
        state = hun.HungarianAlg(np.asarray([[5,51],[445,2],[551,23],[415,566]]))
        step = state.initial_step
    
        while type(step) is not tuple:
            step = step(state)

        self.assertEqual(step[1],7)

    def test_retangular_matrix_with_tie(self):
        state = hun.HungarianAlg(np.asarray([[5,51],[5,10],[551,23],[415,566]]))
        step = state.initial_step
    
        while type(step) is not tuple:
            step = step(state)

        self.assertEqual(step[1],15)

    def test_zero_cost_matrix(self):
        state = hun.HungarianAlg(np.asarray([[0,0],[0,0],[0,0],[0,0]]))
        step = state.initial_step
    
        while type(step) is not tuple:
            step = step(state)

        self.assertEqual(step[1],0)

if __name__ == '__main__':
    unittest.main()