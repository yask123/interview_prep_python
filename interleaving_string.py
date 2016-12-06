'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Subscribe to see which companies asked this question
'''


def is_interleaved(s1, s2, s3, a_index, b_index, c_index):
    if c_index == len(s3):
        return True
    elif a_index < len(s1) and b_index < len(s2) and s3[c_index] == s1[a_index] and s3[c_index] == s2[b_index]:
        if is_interleaved(s1, s2, s3, a_index + 1, b_index, c_index + 1):
            return True
        if is_interleaved(s1, s2, s3, a_index, b_index + 1, c_index + 1):
            return True
        return False
    elif a_index < len(s1) and s3[c_index] == s1[a_index]:
        return is_interleaved(s1, s2, s3, a_index + 1, b_index, c_index + 1)
    elif b_index < len(s2) and s3[c_index] == s2[b_index]:
        return is_interleaved(s1, s2, s3, a_index, b_index + 1, c_index + 1)
    else:
        return False


s1 = "aabcc "
s2 = "dbbca"

s3 = "aadbbbaccc"

print is_interleaved(s1, s2, s3, 0, 0, 0)
