val = [60, 100, 120]
wt = [10, 20, 30]

def knasp_sack(val, wt, current_index, current_weight, cache = {}):
    if current_index in cache and current_weight in cache[current_index]:
        return cache[current_index][current_weight]
    if current_weight < 0:
        return 0
    if current_index < 0:
        return 0
    if wt[current_index] > current_weight:
        return knasp_sack(val, wt, current_index-1, current_weight)

    a = knasp_sack(val, wt, current_index-1, current_weight - wt[current_index]) + val[current_index]
    b = knasp_sack(val, wt, current_index-1, current_weight)

    if current_index not in cache:
        cache[current_index] = {}
    cache[current_index][current_weight] = max(a,b)


    return cache[current_index][current_weight]

print knasp_sack(val, wt, len(val)-1, 50)
