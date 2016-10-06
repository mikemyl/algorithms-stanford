from ast import literal_eval


class DijkstraPathFinder:

    def __init__(self, input_file):
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                line_content = line.split()
                self.graph[line_content[0]] = [literal_eval(edge) for edge in line_content[1:]]
        print(self.graph)