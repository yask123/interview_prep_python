'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
'''

from collections import deque


def shortest_distance(start, end, dictionary):
    dist = 0
    queue = deque()

    deque.append((start, dist))
    visited = set([start])

    while len(queue):
        popped_word, current_dist = queue.popleft()
        neighbours = get_neighbours(popped_word, dictionary)

        for each_neighbour in neighbours:
            if each_neighbour == end:
                return current_dist + 1

            if each_neighbour not in visited:
                visited.add(each_neighbour)
                queue.append((each_neighbour, dist + 1))


def get_neighbours(word, arr):
    result = []

    for each in arr:
        if is_one_edit_away(word, each):
            result.append(each)
    return result


def is_one_edit_away(startword, endword):
    i = 0
    j = 0
    flag = False

    while i < len(startword) and j < len(endword):
        if startword[i] != endword[j]:
            if flag:
                return False
            flag = True
        i += 1
        j += 1

    if i != len(startword) or j != len(endword):
        return False
    return True


print is_one_edit_away('yask', 'yapk')
