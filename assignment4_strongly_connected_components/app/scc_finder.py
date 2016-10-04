class SccFinder(object):
    def __init__(self, input_file):
        self.scc_list = []
        with open(input_file) as file:
            self.finish_order = []
            self._graph = {}
            for line in file:
                (from_v, to_v) = tuple(number for number in line.split())
                self._add_edge_to_graph(int(from_v), int(to_v))

    def _add_edge_to_graph(self, from_v, to_v):
        if from_v in self._graph:
            self._graph[from_v].append(to_v)
        else:
            self._graph[from_v] = [to_v]
        if to_v in self._graph:
            self._graph[to_v].append(-from_v)
        else:
            self._graph[to_v] = [-from_v]

    def compute_finish_times(self):
        visited_nodes, finished_nodes = set(), set()
        for vertex in self._graph.keys():
            if vertex in visited_nodes:
                continue
            nodes_stack = [vertex]
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (-edge for edge in self._graph[node] if edge < 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
                else:
                    if node not in finished_nodes:
                        self.finish_order.append(node)
                        finished_nodes.add(node)

    def compute_sccs(self):
        visited_nodes = set()
        assert (len(self.finish_order) == len(self._graph))
        for i in reversed(self.finish_order):
            if i in visited_nodes:
                continue
            nodes_stack = [i]
            size = 0
            while nodes_stack:
                node = nodes_stack.pop()
                if node not in visited_nodes:
                    size += 1
                    visited_nodes.add(node)
                    nodes_stack.append(node)
                    neighbors = (edge for edge in self._graph[node] if edge > 0)
                    for neighbor in neighbors:
                        if neighbor not in visited_nodes:
                            nodes_stack.append(neighbor)
            self.scc_list.append(size)
        self.scc_list.sort(reverse=True)
        print(self.scc_list[:5])



