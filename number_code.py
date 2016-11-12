# Given a number return its code. Code is defined as a single digit number which is obtained by repeatedly adding digits of the number till you reach a single digit.

# http://students.codingninjas.in/students/problem?offering_id=137&problem_id=314

def get_code(number):
	while number / 10 != 0:  # while there are more than single digit numbers
		number = get_sum_of_digits(number)
	return number


def get_sum_of_digits(number):
	digit_sum = 0
	while number > 0:
		digit_sum += number % 10
		number = number / 10
	return digit_sum


print get_code(987)
