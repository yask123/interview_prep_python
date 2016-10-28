def solve_maze(maze, row, col, rows, cols):

    if row == rows -1 and col == cols-1:
        maze[row][col] = 'V'
        for each in maze:
            print each
        print '\n'
        return True

    if not in_range(row, col, rows, cols) or maze[row][col] != '1':
        return False

    maze[row][col] = 'V'

    solve_maze(maze, row, col+1, rows, cols)
    down = solve_maze(maze, row+1, col , rows, cols)

    maze[row][col] = '1'
    return False
def in_range(row, col , rows, cols):
    if row >= 0 and row < rows and col >= 0 and col < cols:
        return True
    return False

maze = [
        ['1', '1' , '0', '1'],
        ['1', '1' , '1', '1'],
        ['0', '1' , '0', '1']
      ]
solve_maze(maze, 0,0, len(maze), len(maze[0]))
