
import numpy as np

class HungarianAlg(object):
        
    def __init__(self, cost_matrix):
        '''
        This creates a HungarianAlg object with the cost matrix associated to it. It stores a copy of the matrix as well as the original.
        It then records the shape and initiates some helper variables, like the covers for the rows and columns and the markings.
        '''
        self.O = cost_matrix
        self.C = cost_matrix.copy(deep=True)
        self.n, self.m = self.C.shape
        self.row_covered = np.zeros(self.n, dtype=bool)
        self.col_covered = np.zeros(self.m, dtype=bool)
        self.marked = np.zeros((self.n, self.m), dtype=int)

    def _clear_covers(self):
        '''
        This clears any covers, as they can change meaning from one step to another
        '''
        self.row_covered[:] = False
        self.col_covered[:] = False
    
    def _clear_marks(self):
        '''
        Clears marks when trying new solutions
        '''
        self.marked[:,:] = 0

    def solve(self):
        '''
        This chooses an initial step for the process and then begins following the appropriate steps.
        It saves the assignment solution to self.solution and the final cost found to self.minimum_cost.
        '''
        initial_step = _step0
        if(self.n==self.m):
            initial_step = _step1

        step = initial_step

        while type(step) is not tuple:
            step = step(self)

        if(step[0]):
            self.solution = step[2]
            self.minimum_cost = step[1]
        return step[0]

    def print_results(self):
        '''
        Just a pretty print for the results
        '''
        if self.solution == None:
            raise Exception("No solution was computed yet or there is no solution. Run the solve method or try another cost matrix.")
        for k,v in self.solution.items():
            print("For {} is assignes {}".format(v,k))
        print("The final total cost was {}".format(self.minimum_cost))

def _step0(state):
    '''
    This step pads the matrix so that it's squared
    '''
    matrix_size = max(state.n, state.m)
    pad_columns = matrix_size - state.n
    pad_rows = matrix_size - state.m
    state.C = np.pad(state.C, ((0,pad_columns),(0,pad_rows)), 'constant', constant_values=(0))
    
    state.row_covered = np.zeros(state.C.shape[0], dtype=bool)
    state.col_covered = np.zeros(state.C.shape[1], dtype=bool)
    state.marked = np.zeros((state.C.shape[0], state.C.shape[1]), dtype=int)
    return _step1

def _step1(state):
    '''
    Subtracts the minimum value per column for each cell of that column
    '''
    state.C = state.C - np.min(state.C,axis=1)[:,np.newaxis]
    return _step2

def _step2(state):
    '''
    Subtracts the minimum value per row for each cell of that row
    '''
    state.C = state.C - np.min(state.C,axis=0)[np.newaxis,:]
    return _step3

def _step3(state):
    '''
    This step tries to find a coverage of all zeroes in the matrix using the minimum amount of row/column covers.
    It then uses this coverage to check for a solution. If one is found, the algorithm stops. Otherwise, it goes to step 4 and back to step 3.
    '''
    row_marked = np.zeros(state.C.shape[0], dtype=bool)
    col_marked = np.zeros(state.C.shape[1], dtype=bool)
    
    for j in range(state.C.shape[1]):
        for i in range(state.C.shape[0]):
            if(not state.row_covered[i] and not state.col_covered[j] and state.C[i][j]==0):
                state.marked[i][j] = 1
                state.row_covered[i] = True
                state.col_covered[j] = True
                
    state._clear_covers()
    
    for i in range(state.C.shape[0]):
        if np.sum(state.marked[i,:])==0:
            row_marked[i] = True
            for j in range(state.C.shape[1]):
                if not col_marked[j] and state.C[i][j] ==0:
                    col_marked[j] = True
                    for k in range(state.C.shape[0]):
                        if not row_marked[k] and state.marked[k][j]==1:
                            row_marked[k]=True
    
    state.row_covered = np.logical_not(row_marked)
    state.col_covered = col_marked
    num_lines = np.sum(state.row_covered) + np.sum(state.col_covered)
    
    if num_lines == state.C.shape[0]:
        sol = _check_for_solution(state)
        return sol
    else:
        return _step4

def _step4(state):
    '''
    If no solution was found in step 3, this step changes some values in the matrix so that we may now find some coverage.
    The algorithm may be stuck in a step 3 - step 4 loop. If it happens, there is no solution or the wrong matrix was given.
    '''
    smallest_uncovered = np.inf
    for i in range(state.C.shape[0]):
        for j in range(state.C.shape[1]):
            if not state.row_covered[i] and \
               not state.col_covered[j] and \
               state.C[i][j] < smallest_uncovered:
                smallest_uncovered = state.C[i][j]
                
    for i in range(state.C.shape[0]):
        for j in range(state.C.shape[1]):
            if not state.row_covered[i] and not state.col_covered[j]:
                state.C[i][j] -= smallest_uncovered
            elif state.row_covered[i] and state.col_covered[j]:
                state.C[i][j] += smallest_uncovered
                
    state._clear_covers()
    state._clear_marks()
    return _step3

def _check_for_solution(state):
    '''
    This method uses the coverage of the cost matrix to try and find a solution.
    '''
    for j in range(state.C.shape[1]):
        for i in range(state.C.shape[0]):
            if(not state.row_covered[i] and not state.col_covered[j] and state.C[i][j]==0):
                state.marked[i][j] = 1
                state.row_covered[i] = True
                state.col_covered[j] = True
    sol = {}
    cost = 0
    for i in range(state.n):
        for j in range(state.m):
            if(state.marked[i][j]==1):
                sol[j] = i
                cost = cost + state.O[i][j]
                
    state._clear_covers()

    return len(sol)==state.m, cost, sol