import copy

maze = [[1,1,1,1],
        [0,1,1,0],
        [1,1,1,1]]

result = copy.deepcopy(maze)

def sovle_maze(maze, row, col, result, end_row, end_col):
    if row == end_row and col == end_col and maze[row][col] == 1:
        result[row][col] = '*'
        print result
        return True

    if out_of_bound(row, col, end_row, end_col) or maze[row][col] == 0:
        return False

    result[row][col] = '*'
    if sovle_maze(maze, row, col+1, result, end_row, end_col):
        return True
    if sovle_maze(maze, row+1, col, result, end_row, end_col):
        return True
    result[row][col] = 1

    return False

def out_of_bound(row, col, end_row, end_col):
    if row >= 0 and row <= end_row and col >= 0 and col <= end_col:
        return False
    return True

sovle_maze(maze, 0, 0, result, len(maze)-1, len(maze[0])-1)
