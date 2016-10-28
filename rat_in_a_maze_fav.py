def solve_maze(maze, row, col, max_row, max_col):
    if row == max_row and col == max_col and maze[row][col] == 1:
        return True

    if out_of_bound(maze, row, col) or maze[row][col] == 0:
        return False

    maze[row][col] = '*'
    if solve_maze(maze, row+1, col, max_row, max_col):
        return True
    if solve_maze(maze, row, col+1, max_row, max_col):
        return True
    maze[row][col] = 0
    return False
