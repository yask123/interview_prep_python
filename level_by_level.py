from collections import deque


# Level order traversal for a tree


def breadth_first_search(source, destination):
	node_deqeue = deque([(source, 0)])

	while len(node_deqeue):
		popped_node, level = deque.popleft()
		s

		if popped_node.left:
			if popped_node.left.val == destination:
				return level + 1

			node_deqeue.append(popped_node.left, level + 1)

		if popped_node.right:
			if popped_node.right.val == destination:
				return level + 1

			node_deqeue.append(popped_node.right, level + 1)


# Level order traversal for a graph

def Graph_BFS(source, destination):
	visited = set([source])

	node_deque = deque([source, 0])

	while (len(node_deque) > 0):
		popped_node, level = node_deque.popleft()

		if popped_node.left and popped_node.left not in visited:
			if popped_node.left.val == destination:
				return level + 1
			node_deque.append(popped_node.left, level + 1)

		if popped_node.right and popped_node.right not in visited:
			if popped_node.right.val == destination:
				return level + 1
			node_deque.append(popped_node.right, level + 1)
