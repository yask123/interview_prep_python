def sumx(arr, x):
	start_index = 0
	end_index = len(arr)-1

	while start_index < end_index:
		if arr[start_index] + arr[end_index] < x:
			start_index+=1
		elif arr[start_index] + arr[end_index]>x:
			end_index-=1
		else:
			print arr[start_index],arr[end_index]
			return

sumx([1,2,3,4,5],4)
