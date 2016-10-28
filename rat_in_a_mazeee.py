maze = [[1,1,1,1,1,1,1],
    [1,0,0,1,0,0,1],
    [1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0],
    [1,1,1,1,1,1,1]]

def solve_maze(maze, row, col, rows, cols):
    for each in maze:
        print each
    if row == rows -1 and col == cols-1 and maze[row][col] == 1:
        for each in maze:
            print each
        return True

    if out_of_range(row, col, rows, cols) or maze[row][col] != 1:
        return False

    maze[row][col] = 'V'

    if (solve_maze(maze, row, col+1, rows, cols)):
        return True
    if (solve_maze(maze, row+1, col, rows, cols)):
        return True

    maze[row][col] = 1
    return False
def out_of_range(row, col, rows, cols):
    if row >= rows or row <0 or col <0 or col >= cols:
        return True
    return False
rows = len(maze)
cols = len(maze[0])

print solve_maze(maze,0,0,rows, cols)
