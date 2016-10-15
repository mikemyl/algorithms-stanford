# Programming Assignment 3 - Graph minimum cut
                             

In the third programming assignment we are given [this](app/assignment3.txt) graph
and our goal is to comput the [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut). 

We 've learned a super cool algorithm during this week of the course, the [Karger's algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm)
This is a randomized algorithm, meaning that it does not always produce the correct result, but it's superfast, so
running the same algorithm many times almost guarantees that we ll get the expected result. This was my favourite algorithm
in this course!

Karger's Min Cut algorithm is very simple. Basically it suggests that we remove 1 edge at a time, merging the 2 nodes
that correspond to this edge, until we end up with 2 nodes.

It's pretty easy to code:

```python
class KargerMinCutter:
    def __init__(self, graph_file):
        self._graph = {}
        self._total_edges = 0
        with open(graph_file) as file:
            for index, line in enumerate(file):
                numbers = [int(number) for number in line.split()]
                self._graph[numbers[0]] = numbers[1:]
                self._total_edges += len(numbers[1:])

    def find_min_cut(self):
        min_cut = 0
        while len(self._graph) > 2:
            v1, v2 = self._pick_random_edge()
            self._total_edges -= len(self._graph[v1])
            self._total_edges -= len(self._graph[v2])
            self._graph[v1].extend(self._graph[v2])
            for vertex in self._graph[v2]:
                self._graph[vertex].remove(v2)
                self._graph[vertex].append(v1)
            self._graph[v1] = list(filter(lambda v: v != v1, self._graph[v1]))
            self._total_edges += len(self._graph[v1])
            self._graph.pop(v2)
        for edges in self._graph.values():
            min_cut = len(edges)
        return min_cut

    def _pick_random_edge(self):
        rand_edge = randint(0, self._total_edges - 1)
        for vertex, vertex_edges in self._graph.items():
            if len(vertex_edges) <= rand_edge:
                rand_edge -= len(vertex_edges)
            else:
                from_vertex = vertex
                to_vertex = vertex_edges[rand_edge]
                return from_vertex, to_vertex
```


##### Challenges:

* Pick an edge uniformly at random. We need to pay attention to this, it's not sufficient to pick a random vertex,
and then pick a random edge of this vertex. If a vertex has 10 edges and another has 100 edges, these 110 edges don't
get selected under equal possibilities.
* Run the algorithm as many times as needed (define how many?), to guarantee that the min cut is going to be indeed the min.

##### Solver:

* [min_cutter.py](app/min_cutter.py)

##### Unittests:

* [test_min_cutter.py](test/test_min_cutter.py)
