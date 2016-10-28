arr =  [13, 7, 6, 12]

def next_greater_number(arr):
    stack = []
    result = []
    for i in range(len(arr)-1, -1,-1):
            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()
            if len(stack):
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(arr[i])
    result.reverse()
    return result

print next_greater_number(arr)
