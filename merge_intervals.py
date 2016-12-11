def merge(interval, new_interval):
    next_index = 0
    for i, each_interval in enumerate(interval):
        if each_interval[0] > new_interval[0]:
            next_index = i
            break
    if i > 0:
        merged = merge_three(interval[next_index - 1], new_interval, interval[next_index])

        if merged != None:
            return merged + new_interval[next_index + 1:]

    merged = merge_two(new_interval, interval[next_index])
    if merged != None:
        return interval[: next_index] + [merged] + interval[next_index + 1:]

    if i > 0:
        merged = merge_two(interval[next_index - 1], new_interval)
        if merged != None:
            return interval[:next_index - 1] + [merged] + interval[next_index:]

    return interval[:next_index] + [new_interval] + interval[next_index:]


def merge_three(prev_interval, new_interval, next_interval):
    if new_interval[0] <= prev_interval[1] and new_interval[1] >= next_interval[0]:
        start_time = prev_interval[0]
        end_time = max(new_interval[1], next_interval[1])
        return [start_time, end_time]

    return None


def merge_two(prev_interval, new_interval):
    if prev_interval[1] >= new_interval[0]:
        return [prev_interval[0], max(prev_interval[1], new_interval[1])]

    return None


interval = [[1, 4], [6, 10]]

new_interval = [2, 5]

print merge(interval, new_interval)
