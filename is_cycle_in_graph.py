import graph


def is_cycle(input_graph):
    visited = set()

    for i in range(len(input_graph)):
        rec_stack = set()
        if _is_cycle_util(input_graph, i, visited, rec_stack):
            return True
    return False


def _is_cycle_util(input_graph, i, visited, rec_stack):
    if i not in visited:
        visited.add(i)
        rec_stack.add(i)

        for each_neighbour in input_graph[i]:
            if each_neighbour in rec_stack:
                return True
            elif each_neighbour not in visited and _is_cycle_util(input_graph, each_neighbour, visited, rec_stack):
                return True

    if i in rec_stack:
        rec_stack.remove(i)
    return False


g = graph.Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print is_cycle(g.nodes)
