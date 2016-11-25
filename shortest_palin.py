'''
O(n^2) solution, can be improved to O(n)
'''


def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    index = 0
    while not_palin(s):  # O(n)
        s = s[:index] + s[len(s) - index - 1] + s[index:]  # O(n)
        index += 1
    return s


def not_palin(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return True
        i += 1
        j -= 1
    return False


inp = 'somerandomstring'
print shortestPalindrome(inp)