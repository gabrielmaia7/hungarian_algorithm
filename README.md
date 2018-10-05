# The Hungarian Algorithm

## What?

This repo contains a crude, but a good shot at, an implementation in Python of the Hungarian Algorithm (or the Munkres Assignment ALgorithm); one of the coolest algorithms I've studied in graph theory (you can't say it isn't).
For a full description of the algorithm and its theoretical basis, visit the [Wikipedia link](https://en.wikipedia.org/wiki/Hungarian_algorithm]).<br>

In short, the Hungarian Algorithm (or Method) aims at solving a specific kind o problem, which is an assignment problem. More so, it tries to solve it in polynomial time, which is the most compelling reason to use it.
An assignment problem consists mainly on associating a group of tasks *T* to a set of workers *W*, while considering the cost matrix *C*, which describes the cost *C[i,j]* of assigning task *T[i]* to worker *W[j]*.

This means that the algorithm solves the minimum cost - or the maximum gain, if you think about it differently - of a task assignment situation. This works when combining teams, passing down processing tasks to workers in a system, calculating delivery routes for drivers or service workers, you name it: if it can be reduced to an assignment problem, this is your guy.

When I said I studied it in graph theory, it's because, as I said, problems that can be reduced to an assignment problem can also be solved with the Hungarian. One of these is finding a perfect matching with minimal cost (or maximum gain) in a complete bipartite weighted graph, where partition *T* is the tasks and partition *W* the workers. 

A matching would be a group of edges with no common vertices among them, and a perfect matching would be one that touches all vertices in the graph. So, in our graph, a perfect matching would associate every vertice in *T* to a sole vertice in *W*, and vice-versa. That's an assignment problem.

## Why?

It's a common enough problem and a simple enough algorithm for me to train my python skills. So I end up with a code that, who knows, may just be useful for me, and I have some fun while I'm at it.

There are two main ways to see this method, as a problem in graphs, if your costs are a complete bipartite graph, or as a problem in matrix, if your costs are in a matrix. Since dealing with matrices in python is much more intuitive, we go with matrices, specifically the method presented in the Wikipedia page.

So, if you want to contribute, feel free to propose an implementation using graphs!

## How?

Simply import hungarian.py as a module. It contains a class HungarianAlg and some internal functions that you shouldn't mind. 
The use is documented in the code itself, which is not long, and proper use can be seen in the hungarian_test.py file. Run this test file to make sure the algorithm works.