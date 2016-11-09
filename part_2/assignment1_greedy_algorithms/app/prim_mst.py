from util.heap import IndexedMinHeap


class PrimMST:
    def __init__(self, graph_file):
        self._graph = {}
        self._cost = 0
        with open(graph_file, "r") as file:
            num_vertices, num_edges = (int(num) for num in file.readline().split())
            for i in range(1, num_vertices + 1):
                self._graph[i] = []
            for i in range(num_edges):
                from_vertex, to_vertex, weight = (int(num) for num in file.readline().split())
                self._graph[from_vertex].append((to_vertex, weight))
                self._graph[to_vertex].append((from_vertex, weight))
        self._compute_mst()

    def get_cost(self):
        return self._cost

    def _compute_mst(self):
        unvisited = set(self._graph.keys())
        heap = IndexedMinHeap(key=lambda x: x[1], custom_hash=lambda x: x[0])
        visited = set()
        visited.add(1)
        heap.insert((1, 0))
        while unvisited:
            new_vertex = heap.pop()
            self._cost += new_vertex[1]
            unvisited.remove(new_vertex[0])
            visited.add(new_vertex[0])
            for edge in self._graph[new_vertex[0]]:
                if edge[0] not in visited:
                    if heap.contains(edge):
                        if heap.value_of(edge) >= edge[1]:
                            heap.delete(edge)
                            heap.insert(edge)
                    else:
                        heap.insert(edge)

if __name__ == "__main__":
    prim = PrimMST("assignment_1.2.txt")
    print(prim.get_cost())