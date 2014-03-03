#largest prime factor of 600851475143
def is_prime(number):
	for i in xrange(2, number / 2):
		if number % i == 0:
			return False
		else:
			continue
	return True		

def factors(number):
	return [x for x in xrange(2, (number / 2) + 1) if number % x == 0]


def prime_factors(number):
	return [x for x in factors(number) if is_prime(x)]

print max(prime_factors(600851475143))
