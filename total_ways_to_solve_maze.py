def maze_solve_total_ways(board,row, col, max_row, max_col, cache = {}):
    if row in cache and col in cache[row]:
        return cache[row][col]

    if row == max_row and col == max_col and board[row][col] == 1:
        return 1

    if out_of_bound(row, col, max_row, max_col):
        return 0

    result =  (maze_solve_total_ways(board, row+1, col,max_row, max_col) + maze_solve_total_ways(board, row, col+1, max_row, max_col))
    if row not in cache:
        cache[row] = {}
    cache[row][col] = result
    return cache[row][col]

    
