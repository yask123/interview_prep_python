def permute( A):
	return _helper_permute(A, [], [])

def _helper_permute( remaining, prefix, result):
	
	if remaining == []:
		result.append(prefix)
	
	for i in range(len(remaining)):
		rem = remaining[0:i] + remaining[i+1:]
		_helper_permute(rem, prefix + [remaining[i]], result)
	
	return result

print (permute([ 1, 2, 3 ]))