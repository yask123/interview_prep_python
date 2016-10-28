arr = [['a', 'b', 'c'], ['d', 'e','f'], ['g', 'h', 'i']]

def phone_comb(arr, current_list, result ):

	if current_list >= len(arr):
		print (result)
		return 

	for each_char in arr[current_list]:
		phone_comb(arr, current_list+1, result + each_char)

print (phone_comb(arr, 0,''))

arr = [['a', 'b', 'c'], ['d', 'e','f']]
