'''[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
'''


def search_word(board, word):
	rows = len(board)
	cols = len(board[0])

	for i in range(rows):
		for j in range(cols):
			if board[i][j] == word[0]:
				if dfs(board, i, j, rows, cols, word, 0):
					return 1
	return -1


def dfs(board, row, col, total_rows, total_cols, word, current_word_index):
	if out_of_range(row, col, total_rows, total_cols):
		return False
	if current_word_index == len(word):
		return True

	if board[row][col] != word[current_word_index]:
		return False

	x = dfs(board, row, col + 1, total_rows, total_cols, word, current_word_index + 1)
	if x:
		return True

	x = dfs(board, row, col - 1, total_rows, total_cols, word, current_word_index + 1)
	if x:
		return True

	x = dfs(board, row + 1, col, total_rows, total_cols, word, current_word_index + 1)

	if x:
		return True

	x = dfs(board, row - 1, col, total_rows, total_cols, word, current_word_index + 1)
	if x:
		return True

	return False


def out_of_range(row, col, rows, cols):
	if row >= 0 and row < rows and col >= 0 and col < cols:
		return False
	return True
