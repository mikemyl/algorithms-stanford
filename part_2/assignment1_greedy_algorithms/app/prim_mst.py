from util.heap import IndexedMinHeap


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
                self._graph[to_vertex].append((from_vertex, weight))
        self._compute_mst()

    def _compute_mst(self):
        unvisited = set(self._graph.keys())
        heap = IndexedMinHeap(key=lambda x: x[1])
        visited = set()
        visited.add(1)
        heap.insert((1, 0))
        while unvisited and len(heap._heap) >= 1:
            new_vertex = heap.pop()
            if new_vertex[0] in visited:
                continue
            unvisited.remove(new_vertex[0])
            visited.add(new_vertex[0])
            for edge in self._graph[new_vertex[0]]:
                if edge[0] not in visited:
                    if heap.contains(edge) and heap.value_of(edge) > edge[1]:
                        heap.delete(edge)
                    heap.insert(edge)



if __name__ == "__main__":
    prim = PrimMST("assignment_1.2.txt")