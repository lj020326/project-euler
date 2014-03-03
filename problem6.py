#The difference between the sum of the squares of the first one hundred natural numbers and the squares ofthe sum.

print ((sum(range(1, 101))) ** 2) - sum([x*x for x in range(1, 101)])
