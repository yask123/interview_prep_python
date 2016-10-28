'''
Write a program to count all the possible paths from top left to bottom right of a MXN matrix
with the constraints that from each cell you can either move only to right or down
'''

def count_paths(matrix, row, col, total_rows, total_cols):
	if row == total_rows -1 and col == total_cols -1:
		return 1

	if out_of_range(row, col, total_rows, total_cols):
		return 0

	return count_paths(matrix, row, col+1, total_rows, total_cols) + \
		count_paths(matrix, row+1, col, total_rows, total_cols)

def out_of_range(row, col, total_rows, total_cols):
	if row < 0 or row >= total_rows or col <0 or col >= total_cols:
		return True
	return False

