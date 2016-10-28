def decrypt(input_str, k = 0):
    if k >= 26:
        k = k % 26
    result = ''
    for each_char in input_str:
        index = ord(each_char) -  ord('a') - k
        if index < 0:
            index = ord('z')  + index + 1
            result += chr(index)
        else:
            result += chr(ord('a') + index)
    return result


print decrypt('abc',1)

print decrypt('zab',-1)
