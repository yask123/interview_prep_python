
def pow(a,n):
	if n <0:
		return None
	elif n  == 1:
		return a
	elif n == 0:
		return 1

	if n%2 == 0:

		temp = pow(a,int(n/2))
		return temp * temp
	else:
		temp_a = pow(a,int(n/2))
		temp_b = pow(a,n-int(n/2))
		return temp_a * temp_b

print (pow(2,5))