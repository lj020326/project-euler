#largest palindrome made from the product of two 3 digit numbers
def is_palindrome(number):
	return str(number) == str(number)[::-1]
def largest_palindrome(number):
	return [x for x in range(number + 1) if is_palindrome(x)]

print largest_palindrome(999 * 999)

