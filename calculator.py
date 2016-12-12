'''

Expression evaluator

3 * 4 + 6

values = 12 6

op =  +
result =
'''


def calculator(expression):
    value_stack = []
    operator_stack = []

    for each in expression:
        if ord(each) <= ord('9') and ord(each) >= ord('0'):
            value_stack.append(each)

        else:
            while len(operator_stack) > 0 and rank(operator_stack[-1]) >= each:
                a = value_stack.pop()
                b = value_stack.pop()

                op = operator_stack.pop()

                value_stack.append(calc(a, b, op))

            operator_stack.append(each)

    while len(operator_stack) > 0:
        a = value_stack.pop()
        b = value_stack.pop()
        op = operator_stack.pop()
        value_stack.append(calc(a, b, op))

    return value_stack[0]


def rank(op):
    ranks_map = {'+': 0, '-': 0, '*': 1, '/': 1}
    return ranks_map[op]


def calc(a, b, op):
    a = int(a)
    b = int(b)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b

    elif op == '*':
        return a * b

    elif op == '/':
        return a / b


print calculator(['3', '*', '4', '+', '6'])
