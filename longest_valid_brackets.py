def get_longest_length(arr):
    stack = []
    start_index = 0
    end_index = 0
    max_length = 0
    while end_index < len(arr):
        if is_opening(arr[end_index]):
            stack.append(arr[end_index])
            end_index+=1
        else:
            if len(stack) > 0:
                popped_bracket = stack.pop()
                if corresponding_opening_bracker(arr[end_index]) == popped_bracket:
                    end_index += 1
            else:
                max_length = max(max_length, (end_index - start_index))
                start_index = end_index +1
                end_index += 1
    max_length = max(max_length, (end_index - start_index))
    return max_length

def is_opening(bracket):
    openin_brackets = set(['(','[','{'])
    if bracket in openin_brackets:
        return True
    return False

def corresponding_opening_bracker(closing_bracket):
    bracket_map = {')':'('}
    return bracket_map[closing_bracket]

print get_longest_length('(')
