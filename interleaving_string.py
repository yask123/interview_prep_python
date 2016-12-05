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


def is_interleaved(s1, s2, s3):
    a_index = 0
    b_index = 0
    c_index = 0

    while c_index < len(s3):

        if a_index < len(s1) and s1[a_index] == s3[c_index]:
            a_index += 1

        elif b_index < len(s2) and s2[b_index] == s3[c_index]:
            b_index += 1

        else:
            return False
        c_index += 1

    return True


s1 = "a a b c c "
s2 = "d b b ca"

s3 = "a a d b b c b c ac"

print is_interleaved(s1, s2, s3)
