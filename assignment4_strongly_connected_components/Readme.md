# Programming Assignment 4 - Strongly Connected Components in a graph
                             

In the fourth programming assignment we are given [this](app/assignment_4.txt) graph
and our goal is to compute the [strongly connected components](https://en.wikipedia.org/wiki/Strongly_connected_component). 

We 've seen in course how to utilize the DFS algorithm (2 times) in order to compute the scc's:
- The first DFS pass computes the finish times of each vertex
- The second DFS computes the scc's


##### Solver:

* [scc_finder.py](app/scc_finder.py)

##### Unittests:

* [test_scc_finder.py](test/test_scc_finder.py)
