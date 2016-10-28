'''
Input: "4+(4-(2+1))"
Output: 5
'''

def infix_to_postfix(expression):
    expression  = expression.split(' ')
    output = []
    stack = []
    for each in expression:
        if is_operator(each):
            print stack
            while len(stack) > 0 and  rank(each) < rank(stack[-1]) > 0:
                output.append(stack.pop())
            stack.append(each)
        else:
            output.append(each)
    while len(stack) > 0:
        output.append(stack.pop())
    return output

def is_operator(expr):
    if expr == '+' or expr == '-' or expr == '*' or expr == '/' :
        return True
    return False

def rank(operator):
    op_map = {'+':0, '-':0, '/':1, '*':2, '(':3, ')':3}
    return op_map[operator]

expression = 'a + b * ( c - e )'

print infix_to_postfix(expression)
