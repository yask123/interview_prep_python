def lengthOfLastWord(A):
    if len(A) <= 1:
        return len(A)
    index = len(A) - 1

    while A[index] == ' ' and index >= 0:
        index -= 1
    end_index = index
    if end_index == - 1:
        return 0
    while A[index - 1] != ' ' and index > 0:
        index -= 1
    start_index = index

    return (end_index - start_index) + 1


A = "yask  "

print lengthOfLastWord(A)
