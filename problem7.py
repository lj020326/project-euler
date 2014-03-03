#finding the 10001 prime

def is_prime(number):
	if number == 2:
		return True
	if not number & 1:
		return False
	for x in range(3, int(number ** 0.5) + 1, 2):
		if number % x == 0:
			return False
	return True

print [x for x in range(2, 200000) if is_prime(x)][10000]
	
