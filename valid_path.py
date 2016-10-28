

def simplify_path(path):
	path = path.split('/')
	stack = []

	for each in path:
		if each == '.':
			continue
		elif each == '..':
			stack.pop()
			
		elif each != '':
			stack.append(each)
		else:
			continue
	return '/'+ '/'.join(stack)

path ="/home/"

print (simplify_path(path))


