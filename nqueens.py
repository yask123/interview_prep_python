def total_queens(n):
    board = [[0 for each in n] for each in n]
    return get_comb(board, n-1)

def get_comb(board,current_col):
    if current_col <0:
        print (board)
        return True
    for each_row in board[current_col]:
        board[each_row][current_col] = 'Q'
        if is_valid(board, each_row, current_col):
            get_comb(board, current_col-1)
        board[each_row][current_col] = '0'

def is_valid(board, row, col):
    #Check upper diagonal
    current_row = row-1
    current_col = col+1

    while current_row >= and current_col <= n-1:
        if board[current_row][current_row] == 'Q':
            return False
        current_col+=1
        current_row-=1

    #Check lower diagonal
    current_row = row+1
    current_col = col+1

    while current_row <= n-1 and current_col <= n-1:
        if board[current_row][current_col] == 'Q':
            return False
        current_row+=1
        current_col+=1

    #Check current row
    current_row = row
    current_col+=1
    while current_col <= n-1:
        if board[current_row][current_col] == 'Q':
            return False
        current_col+=1
