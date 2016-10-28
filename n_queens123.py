def solve_n_queen(board, current_col, rows, cols):
    if current_col < 0:
        return True

    for each_row in len(rows):
        board[each_row][col] = 'Q'
        if is_safe(board[each_row][current_col]):
            solve_n_queen(board, current_col-1, rows, cols)
        board[each_row][col] = ''
    return False
