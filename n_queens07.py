
def solve_nqueens(board, col, rows, cols):

    if col <0:
        for each in board:
            print each
        print '\n'
        return True

    for each_row in range(rows):
        board[each_row][col] = 'Q'
        if is_safe(board, each_row, col, rows, cols):
            x = solve_nqueens(board, col-1, rows, cols)
            if x:
                return x
        board[each_row][col] = ''

    return False

def is_safe(board, row, col , rows, cols):
    for i in range(col+1, cols):
        if board[row][i] == 'Q':
            return False

    row_index = row + 1
    col_index = col + 1

    while row_index < rows and col_index < cols:
        if board[row_index][col_index] == 'Q':
            return False
        row_index += 1
        col_index += 1

    row_index = row - 1
    col_index = col + 1

    while row_index >=0 and col_index < cols:
        if board[row_index][col_index] == 'Q':
            return False
        row_index -= 1
        col_index += 1

    return True

board = [['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','','']]
solve_nqueens(board, len(board[0])-1, len(board), len(board[0]))
