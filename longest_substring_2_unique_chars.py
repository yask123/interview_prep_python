def longest_substring(input_string):
    input_set = set()
    i = 0
    max_length = 0
    current_length = 0
    start_index = 0
    end_index = 0
    while i < len(input_string):
        input_set.add(input_string[i])
        if len(input_set) > 2:
            max_length = max(max_length, current_length)
            print input_string[start_index:end_index+1] , max_length
            input_set = set()
            current_length = 1
            i = start_index +1
            start_index = i
            end_index = i
        else:
            current_length += 1
            end_index = i
        i+=1
    return max_length
input_string = 'abbbcccbcbddeeffffabbbcbc'

print longest_substring(input_string)
