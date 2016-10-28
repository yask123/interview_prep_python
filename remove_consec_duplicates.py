'''
Remove consecutive duplicates from a string recursively. For example, convert "aabccba" to "abcba".
'''

def remove_dups(arr, prev , current, result):
	if current == len(arr):
		return result

	if prev == -1 or arr[prev] != arr[current]:
		return remove_dups(arr,current, current+1, result+arr[current])
	else:
		return remove_dups(arr, current, current+1, result)

print remove_dups('aabccba', -1, 0, '')