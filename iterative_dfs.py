import graph


def dfs(source, adj_graph, visited):
    stack = [source]

    visited.add(source)

    while len(stack):
        popped_v = stack.pop()

        print popped_v

        for each_neighbour in adj_graph[popped_v]:
            if each_neighbour not in visited:
                stack.append(each_neighbour)


def complete_dfs(source, adj_graph):
    visited = set()
    for each in adj_graph:
        if each not in visited:
            dfs(each, adj_graph)


g = graph.Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)

dfs(0, g.nodes)
