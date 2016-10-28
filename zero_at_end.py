def zero_at_end(num): #O(n)
	j =0
	for i,each in enumerate(num):
		if each != 0:
			num[j] = each
			j+=1
	while j < len(num):
		num[j] = 0
		j+=1
	return num


num = [5,0,9,0,653,2,1,0]

print zero_at_end(num)

