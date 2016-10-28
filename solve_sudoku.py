def solve_sudoku(board, row, col):
	if col < 0:
		return True
	if board[row][col] == '':
		for i in range(1, 10):
			board[row][col] = i
			if is_valid(board):
				if row < n - 1:
					x = solve_sudoku(board, row + 1, col)
					if x:
						return x
				else:
					x = solve_sudoku(board, 0, col - 1)

				if x:
					return x

	return False
