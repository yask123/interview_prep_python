# 1 - > n-1A
''' This algo can also be used to sort nos in linear time O(n)'''

def missing_no(num): #O(n)
	i=0
	size = len(num)

	while i < size:
		if num[i] -1 != i and num[i] < size-1 and num[i] > 0:
			num[num[i]-1], num[i] = num[i], num[num[i]-1]
			i-=1
		i+=1

	for i,each in enumerate(num):
		if i != each-1:
			return each



print missing_no([3,-4,1])


