'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''


def sub_concat_results(s, words):
    temp_set = set(words)
    results = []
    f_s = 0

    while f_s < len(s):
        t_s = f_s
        t_e = f_s + 1
        while t_e < len(s) and len(temp_set) > 0:
            if s[t_s:t_e + 1] in temp_set:
                temp_set.remove(s[t_s:t_e + 1])
                t_s = t_e + 1
                t_e = t_s + 1
            else:
                t_e += 1

        if len(temp_set) == 0:
            results.append(f_s)
            f_s = t_s
            temp_set = set(words)
        else:
            f_s = t_s + 1

    return results


s = "barfoothefoobarman"

words = ["foo", "bar"]

print sub_concat_results(s, words)
