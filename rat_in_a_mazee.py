import copy
maze = [[1,1,1,0],
        0,0,1,0]]

result = copy.deepcopy(maze)

def solve_maze(maze, row, col, final_row, final_col, result):
    if row == final_row and col == final_col and maze[row][col] == 1:
        result[row][col] = '*'
        print result
        return True

    if out_of_bound(row,col, final_row, final_col) or maze[row][col] == 0:
        return False

    maze[row][col] = '*'

    if solve_maze(maze,row, col+1, final_row, final_col, result):
        return True
    if solve_maze(maze,row+1, col, final_row, final_col, result):
        return True

    maze[row][col] = 1
    return False
