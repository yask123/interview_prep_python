import random
from collections import deque


class Node:
    def __init__(self, id):
        self.id = id
        self.links = []


class Graph:
    def __init__(self):
        self.nodes = []

    def create_graph(self):
        for i in range(9):
            self.nodes.append(Node(i))

        for i in range(9):
            self.nodes[i].links.append(self.nodes[random.randint(0, 8)])

    def dfs(self, source_id):
        source = self.nodes[source_id]
        return self._dfs

    def _dfs(self, node):

        if node == None:
            return
        for each_neighbour in node.links:
            self._dfs(each_neighbour)

    def bfs(self, source_id):
        queue = deque([self.nodes[source_id]])

        while len(queue):
            popped_node = queue.popleft()
            for each_neighbour in popped_node.links:
                queue.append(each_neighbour)
