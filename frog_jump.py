# coding=utf-8
"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

"""


def is_possible(frog_pos, current_index, arr, last_jump):
    if frog_pos == arr[current_index] and current_index == len(arr) - 1:
        return True

    elif frog_pos == arr[current_index]:
        if is_possible(frog_pos + last_jump + 1, current_index + 1, arr, last_jump + 1):
            return True
        elif last_jump > 0 and is_possible(frog_pos + last_jump - 1, current_index + 1, arr, last_jump - 1):
            return True
        elif last_jump > 0 and is_possible(frog_pos + last_jump, current_index + 1, arr, last_jump):
            return True
        else:
            return False

    elif frog_pos > arr[current_index]:
        try:
            jump_index = arr.index(frog_pos)
            return is_possible(frog_pos, jump_index, arr, last_jump)
        except:
            return False
    else:
        return False


arr = [0, 1, 3, 5, 6, 8, 12, 17]

print is_possible(0, 0, arr, 0)
