'''
https://www.hackerrank.com/challenges/linkedin-practice-binary-numbers
'''
bin_number = (bin(1999))[2:]
print (bin_number)
max_count = 0
count = 0

for i in range(len(bin_number)):
    if bin_number[i] == '1':
        count+=1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print (max_count)
