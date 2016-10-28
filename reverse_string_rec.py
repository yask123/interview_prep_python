def reverse(input_string, n, string_length, result):
    if n == string_length:
        return None
    reverse(input_string, n+1, string_length, result)
    result.append(input_string[n])

    return result

def reverse_string(input_string):
    return ''.join(reverse(input_string,0,len(input_string), []))

print reverse_string('yask')
