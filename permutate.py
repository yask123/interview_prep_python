
def perm(word):
	_perm_helper(word, '')


def _perm_helper(remaining, prefix):

	if len(remaining) == 0:
		print prefix

	for i in range(len(remaining)):
		rem = remaining[0:i] + remaining[i+1:]
		_perm_helper(rem, prefix+remaining[i])



