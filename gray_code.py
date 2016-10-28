def gray_comb( arr_list, current_list, comb, result):
	if current_list < 0:
		result.append(comb)
		return 

	for each_bit in arr_list[current_list]:
		gray_comb(arr_list, current_list-1, comb+str(each_bit), result)
	return result

bin_comb =  (gray_comb([[0,1],[0,1], [0,1]], 2, '', []))

n = 5
total_nos = n**2 -1
for i in range(total_nos):
	print (i)