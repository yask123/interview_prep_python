'''
Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ
'''


def is_word(string, boggle):
    m, n = len(boggle), len(boggle[0])

    for i in range(m):
        for j in range(n):
            if dfs(boggle, i, j, string, 0):
                return True


def dfs(boggle, row, col, string, string_index):
    if string_index == len(string):
        return True
    if row < 0 or row >= len(boggle) or col < 0 or col >= len(boggle[0]):
        return False

    if boggle[row][col] != string[string_index]:
        return False

    if dfs(boggle, row, col + 1, string, string_index + 1):
        return True
    if dfs(boggle, row + 1, col, string, string_index + 1):
        return True
    if dfs(boggle, row + 1, col + 1, string, string_index + 1):
        return True
    if dfs(boggle, row - 1, col - 1, string, string_index + 1):
        return True

    return False
