

def next_perm(num):
	if len()
	i = len(num) -1

	while i >= 0:
		if num[i-1] < num[i]:

			break_num = num[i-1]
			#Find no just greater than this break_num
			lowest_index = None
			for j in range(i, len(num)):
				if num[j] > break_num:
					just_greaterthan_break_index = j
					if lowest_index == None or num[lowest_index] > num[just_greaterthan_break_index]:
						lowest_index = j
			#Swap break_num and just_greaterthan_break
			num[i-1], num[lowest_index] = num[lowest_index], num[i-1]

			#Sort nums from [i - len(num-1)]
			return num[:i] + sorted(num[i:])
		i -=1

print (next_perm([1,2]))
