arr = [ [1, 0 , 0 , 0 , 1],
		[1, 0 , 0 , 0 , 1],
		[1, 0 , 0 , 0 , 1],
		[1, 1 , 1 , 1 , 1]
	  ]

def solve_maze(arr, current_row, current_col, sol):
	if is_destination(arr, current_row, current_col):
		sol[current_row][current_col] = '*'
		return True
	if is_out_of_bound(arr, current_row, current_col) or arr[current_row][current_col] == 0:
		return False

	sol[current_row][current_col] = '*'

	if solve_maze(arr,current_row,  current_col+1, sol):
		return True

	if solve_maze(arr, current_row+1, current_col, sol):
		return True

	sol[current_row][current_col] = '1'
	return False

def is_destination(arr, current_row, current_col, sol):
	if current_row == len(arr)-1 and current_col == len(arr[0])-1 and arr[current_row][current_col] == 1:
		return True
	return False

