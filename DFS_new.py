class Node:
    def __init__(self, value, neighbours = []):
        self.neighbours = neighbours
        self.value = value


class Graph:
    def __init__(self, nodes = []):
        self.nodes = []

    def dfs_search(self, source_node, visited = set()):

        if source_node == None:
            return None
        visited.add(source_node)
        print source_node.value,

        for each_neighbour in source_node.neighbours:
            if each_neighbour not in visited:
                self.dfs_search(each_neighbour)

    def BFS(self, source_node):
        queue = [source_node]
        visited = set()
        visited.add(source_node)

        while len(queue) > 0:
            popped_element = queue.pop()
            print (popped_element.value)
            for each_neighbour in popped_element.neighbours:
                if each_neighbour not in visited:
                    queue.append(each_neighbour)
                    visited.add(each_neighbour)




a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.neighbours = [b,c]
b.neighbours = [d]

my_graph = Graph([a,b,c,d])
my_graph.dfs_search(a)

