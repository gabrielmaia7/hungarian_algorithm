#Python 3.6 was used
'''
This task is a classic case of an assignment problem, whose solution lies in finding a minimum weight
perfect matching in a weighted bipartite graph, where the weights are the assignment costs, and the
two partitions are the workers and tasks to be assigned to each other. One simple algorithm that can
solve this problem is the Hungarian Algorithm (https://en.wikipedia.org/wiki/Hungarian_algorithm).
The implementation used here is taken from the wiki page of the algorithm.
'''

import numpy as np
import math as m
import task_utils as utils
import hungarian as hun

def pretty_print_results(sol, cols, rows):
    for k,v in sol[2].items():
        print("For "+rows[v]+ " is assigned "+cols[k])
    print("The final total cost was "+ str(sol[1]))

def main():
    try:
        cargo, trucks = utils.loadData('data')
    except FileNotFoundError as e:
        raise utils.task_exception("Data on cargo and/or truck location is not on the correct file, please correct that and try again",e)
        
    cargo_names, trucks_names = cargo.values[:,0], trucks.values[:,0]

    try:
        C = utils.getCostMatrix(cargo.values,trucks.values)
    except Exception as e:
        raise utils.task_exception("Cost matrix not loaded properly. Check if cargo and/or truck files are properly",e)
        
    state = hun.HungarianAlg(C)
    
    step = state.initial_step
    
    while type(step) is not tuple:
        step = step(state)

    pretty_print_results(step,cargo_names,trucks_names)

if __name__ == '__main__':
    try:
        main()
    except utils.task_exception as e:
        print(e)
