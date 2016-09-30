
class MinCutter:
    def __init__(self, graph_file):

        with open(graph_file) as file:
            self._graph = {}
            for index, line in enumerate(file):
                numbers = [number for number in map(int, line.split())]
                self._graph[numbers[0]] = numbers[1:]
        pass

    def get_graph(self):
        print(self._graph)
        return self._graph

