def find_comb(nums, target, current_index, last_index, result):
	if target == 0:
		print (result)
		return 1    
	if current_index > last_index:
		return 0
	
	if target < 0:
		return 0
	
	a = find_comb(nums, target-nums[current_index], current_index, last_index, result + str(nums[current_index]))
	b = find_comb(nums, target, current_index+1, last_index, result)
	
	return a+b

nums = [1, 2, 4]
target = 4

print (find_comb(nums,target,0,2,''))