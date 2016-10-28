[ * , * , * , Q,
[ * , * , * , *]]

def solve_queens(board,current_row):
    if current_row < 0:
        return True

    for each_row in range(len(board)):
        board[each_row][current_row] = 'Q'

        if is_valid(board, current_row, each_row):
            solve_queens(board, current_row-1)

        board[each_row][current_row] = '*'
    return False
