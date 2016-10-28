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

class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        total_length = len(A)*2
        arr = [0]*total_length
        return self.bracker_combinations(0,0,0,arr,A)

    def bracker_combinations(position, open, close, result, total_length):
        if close == total_length:
            final_result.append(''.join(result))
            return None
        else:
            if (open > close):
                result[position] = ')'
                bracker_combinations(position+1, open, close+1, result, total_length, result)
            if open < total_length:
                result[position] = '('
                bracker_combinations(position+1, open+1, close, result, total_length, result)
        return result
