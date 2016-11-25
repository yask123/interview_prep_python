'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''


def solve_sudoku(board, row, col):
	if col < 0:
		return True

	if board[row][col] == '.':
		for i in range(1, 9):
			board[row][col] = i
			if is_valid(board):
				if row < len(board):
					a = solve_sudoku(board, row + 1, col)
					if a:
						return a
				else:
					a = solve_sudoku(board, 0, col - 1)
					if a:
						return a
			board[row][col] = '.'
		return False
