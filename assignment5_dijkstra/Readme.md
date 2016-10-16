# Programming Assignment 5 - Dijkstra Shortest Paths
                             

In the fourth programming assignment we are given [this](app/assignment_5.txt) graph
and our goal is to compute the shortest paths from the vertex that resides in the first line to 
the vertices {7, 37, 59, 82, 99, 115, 133, 165, 188, 197}.


We are supposed to utilize the [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
for this task.

##### Challenges:
* Use a min-heap instead of searching for the min edge at each greedy step of the algorithm. My dijkstra implementation
in python currently searches all edges to find the minimum. Using a min-heap would require us to be able to remove any
element in the heap (it's on the TODO list). This is a small graph, so both implementations will return the 
result immediately, but for larger graphs, using a min-heap would make a huge difference.

##### Solver:

* [dijkstra_path_finder.py](app/dijkstra_path_finder.py)

##### Unittests:

* [test_dijkstra_path_finder.py](test/test_dijkstra_path_finder.py)
