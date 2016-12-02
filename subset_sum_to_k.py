arr = [1, 3, 5]


def subset_sum(arr, pos, target, cache={}):
    key = (pos, target)
    if key in cache:
        return cache[key]

    if target == 0:
        cache[key] = True
        return True
    if target < 0 or pos < 0:
        cache[key] = False
        return False

    cache[key] = subset_sum(arr, pos - 1, target - arr[pos], cache) or subset_sum(arr, pos - 1, target, cache)
    return cache[key]


print subset_sum(arr, len(arr) - 1, 4)
