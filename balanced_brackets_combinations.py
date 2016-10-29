def bracker_combinations(position, open, close, result, total_length):
    if close == total_length:
        print result
        return None
    else:
        if (open > close):
            result[position] = ')'
            bracker_combinations(position+1, open, close+1, result, total_length)
        if open < total_length:
            result[position] = '('
            bracker_combinations(position+1, open+1, close, result, total_length)

arr = [0]*6
bracker_combinations(0,0,0,arr,3)

