def check_valid(expression):
	queue = []
	for each in expression:
		if is_opening(each):
			queue.append(each)
		else:
			if queue[-1] != get_closing_bracket(each):
				return False
			else:
				queue.pop()
	if len(queue) > 0:
		return False
	return True

def is_opening(each):
	if each == '(' or each == '{' or each == '[':
		return True
	return False

def get_closing_bracket(each):
	if each == ')':
		return '('
	elif each == '}':
		return '{'
	elif each == ']':
		return '['
	else:
		print ('error')
		return None

print (check_valid(''))