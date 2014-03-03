#highly divisible triangular number

def triangular_numbers(howmany):
	return [sum(range(1, x + 1)) for x in range(1, howmany + 1)]

def factors_count(number):
	return len([x for x in range(1, number + 1) if number % x == 0])








