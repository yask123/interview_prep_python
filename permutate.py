def permutate(words):
	return _perm_helper(words, '', [])


def _perm_helper(remaining, prefix, result):

	if len(remaining) == 0:
		result.append(prefix)
		return

	for i in range(len(remaining)):
		new_remaining = remaining[:i] + remaining[i + 1:]
		_perm_helper(new_remaining, prefix + remaining[i], result)

	return result


print permutate('abc')
