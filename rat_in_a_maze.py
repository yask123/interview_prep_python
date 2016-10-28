matrix = [[1,1,1,1],
          [1,0,0,1],
          [1,0,0,1],
          [1,1,1,1]]

def out_of_bound(row, col, matrix):
	if row > len(matrix)-1 or col > len(matrix[0])-1:
		return  True
	return False

def solve_maze(current_row, current_col,matrix, ans):
	if current_row == len(matrix)-1 and current_col == len(matrix[0])-1 and matrix[current_row][current_col] == 1:
		ans.append((current_row, current_col))
		return True

	if out_of_bound(current_row, current_col, matrix) or matrix[current_row][current_col] == 0:
		return False

	#Move right ?
	if solve_maze(current_row, current_col+1, matrix,ans):
		ans.append((current_row, current_col))
		return True

	# Move down ?
	if solve_maze(current_row+1, current_col, matrix, ans):
		ans.append((current_row, current_col))
		return True

	return False

ans =  []
solve_maze(0,0,matrix,ans)
print (ans)