'''
Knight tour
'''


def knight_tour(n, row, col, visited):
    if n == 0:
        return True

    if out_of_bound(row, col):
        return False

    neighbours = get_neighbours(row, col)

    for each_neighbour in neighbours:
        if each_neighbour not in visited:
            visited.add(each_neighbour)
            if knight_tour(n - 1, each_neighbour[0], each_neighbour[1]):
                return True

            visited.remove(each_neighbour)
    return False
