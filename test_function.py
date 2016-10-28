def test(prev_node):
    prev_node.pop()
    prev_node.append('yask')

prev_node = ['hello']

test(prev_node)
print prev_node[0]
