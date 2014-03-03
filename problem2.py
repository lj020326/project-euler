#sum of even valued terms of a fibonacci series which not exceeding 4000000

fibonacci = []
first = 1
second = 2
third = first + second
fibonacci.append(1)
fibonacci.append(2)
while third <= 4000000:
	third = first + second
	if third <= 4000000:
		fibonacci.append(third)
		first = second
		second = third		
	else:
		break
result = 0
for x in fibonacci:
	if x % 2 == 0:
		result += x
print result

	
