import sys

class ShortestPathFinder:

    def __init__(self, input_file):
        with open(input_file) as file:
            n_vertices, n_edges = (int(num) for num in file.readline().split())
            self._graph = [None] * (n_vertices + 1)
            self._shortest_paths = [None] * (n_vertices + 1)
            self._shortest_path = sys.maxsize
            for line in file:
                edge_from, edge_to, edge_weight = (int(num) for num in line.split())
                if self._graph[edge_from] is None:
                    self._graph[edge_from] = [(edge_to, edge_weight)]
                else:
                    self._graph[edge_from].append((edge_to, edge_weight))
        for source_vertex in range (1, len(self._graph)):
            if self._compute_shortest_paths(source_vertex) is None:
                self._shortest_paths = None
                break
        else:
            path = sys.maxsize
            for vertex in range(1, len(self._graph)):
                if self._graph[vertex] is None:
                    continue
                for shortest_path in self._shortest_paths[vertex]:
                    if shortest_path < path:
                        path = shortest_path
            self._shortest_path = path
            print(path)

    def _compute_shortest_paths(self, source_vertex):
        self._shortest_paths[source_vertex] = [sys.maxsize] * len(self._graph)
        self._shortest_paths[source_vertex][source_vertex] = 0
        for path_length in range(len(self._graph) - 1):
            for vertex in range(1, len(self._graph)):
                if self._graph[vertex] is None:
                    continue
                for edge in self._graph[vertex]:
                    current_sp = self._shortest_paths[source_vertex][edge[0]]
                    if current_sp > self._shortest_paths[source_vertex][vertex] + edge[1]:
                        self._shortest_paths[source_vertex][edge[0]] = self._shortest_paths[source_vertex][vertex] + edge[1]
        for vertex in range(1, len(self._graph)):
            if self._graph[vertex] is None:
                continue
            for edge in self._graph[vertex]:
                current_sp = self._shortest_paths[source_vertex][edge[0]]
                if current_sp > self._shortest_paths[source_vertex][vertex] + edge[1]:
                    print("Negative Cycle detected")
                    return None
        return True

    def get_shortest_path(self):
        return self._shortest_path



if __name__ == "__main__":
    path_finder = ShortestPathFinder("g1.txt")
    path_finder = ShortestPathFinder("g2.txt")
    path_finder = ShortestPathFinder("g3.txt")