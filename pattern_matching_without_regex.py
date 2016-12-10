'''
Given a string, find out if string follows a given pattern or not without using any regular expressions.

Examples:

Input:
string - GraphTreesGraph
pattern - aba
Output:
a->Graph
b->Trees

Input:
string - GraphGraphGraph
pattern - aaa
Output:
a->Graph

Input:
string - GeeksforGeeks
pattern - GfG
Output:
G->Geeks
f->for

Input:
string - GeeksforGeeks
pattern - GG
Output:
No solution exists
'''


def match(pattern, word, pattern_index, word_index, mapped_chars):
    if word_index == len(word) and pattern_index == len(pattern):
        return True

    if pattern[pattern_index] in mapped_chars:
        substr = mapped_chars[pattern[pattern_index]]
        if substr == word[word_index: word_index + len(substr)]:
            return match(pattern, word, pattern_index + 1, word_index + len(substr), mapped_chars)
        else:
            return False

    for i in range(word_index + 1, len(word)):
        mapped_chars[pattern[pattern_index]] = word[word_index: i]
        if match(pattern, word, pattern_index + 1, i, mapped_chars):
            return True
        del mapped_chars[pattern[pattern_index]]

    return False


print match('aba', 'GeeksforGeeks', 0, 0, {})
