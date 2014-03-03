#longest collatz sequence

def terms_in_collatz_sequence(number):
	a = []
	while number > 1:
		a.append(number)
		if number % 2 == 0:
			number /= 2
		else:
			number = 3 * number + 1
	a.append(1)
	#print a
	return len(a)

def longest_collatz_sequence(number):
	a = {x: terms_in_collatz_sequence(x) for x in range(1, number+1)}
	 
