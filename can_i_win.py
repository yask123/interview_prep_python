'''
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

'''


def can_i_win(current_player, running_total, desired_total, max_choosable_integer, visited):
    if current_player == 1 and running_total >= desired_total:
        return True
    elif current_player == 0 and running_total >= desired_total:
        return False

    for i in range(max_choosable_integer, 0, -1):
        if i not in visited:
            visited.add(i)
            if can_i_win(current_player ^ 1, running_total + i, desired_total, max_choosable_integer, visited):
                return True

    return False


print  can_i_win(0, 0, 11, 10, set())
