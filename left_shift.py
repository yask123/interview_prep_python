from collections import deque

'''
arr = [1,2,3,4,5]
           ^ - end
       ^---
       '''

arr = [1,2,3,4,5]
shift_pad = 0
result = []

for i in range(shift_pad,len(arr)):
    result.append(arr[i])

for i in range(0, shift_pad):
    result.append(arr[i])

print (result)
