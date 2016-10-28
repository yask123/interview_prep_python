'''
1 2 3  >    4 1
4 5 6       5 2
            6 3

current_column = max_column - row
current_row = col
'''
def get_dd_matrix(rows, columns):
    return [[0 for x in range(columns)] for y in range(rows)]

def rotate_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    new_matrix = get_dd_matrix(col,row)

    for each_row in range(row):
        for each_col in range(col):
            new_matrix[each_col][row-each_row-1] = matrix[each_row][each_col]
    return new_matrix

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print (rotate_matrix(matrix))
