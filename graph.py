class Graph:
    def __init__(self, n):
        self.nodes = [[] for each in range(n)]

    def addEdge(self, from_node, to_node):
        self.nodes[from_node].append(to_node)
