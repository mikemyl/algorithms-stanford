class PrimMST:
# 4, 16, -3
    def __init__(self, graph_file):
        self._graph = {}
        with open(graph_file, "r") as file:
            num_vertices, num_edges = (int(num) for num in file.readline().split())
            for i in range(1, num_vertices + 1):
                self._graph[i] = []
            for i in range(num_edges):
                from_vertex, to_vertex, weight = (int(num) for num in file.readline().split())
                self._graph[from_vertex].append((to_vertex, weight))
        self._compute_mst()

    def _compute_mst(self):
        unvisited = set(self._graph.keys())
        visited = set()
        visited.add(1)
        unvisited.remove(1)


if __name__ == "__main__":
    prim = PrimMST("assignment_1.2.txt")