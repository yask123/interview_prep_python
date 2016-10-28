def anagram(s1, s2):
	c1  = [0]*26
	c2  = [0]*26

	for each_char in s1:
		c1[ord(each_char)-ord('a')] += 1

	for each_char in s2:
		c2[ord(each_char) - ord('a')] +=1 
	print (c2)
	for i in range(0,26): # [0 -> 25]
		if c1[i] != c2[i]:
			return False
	return True

print (anagram('yask', ''))