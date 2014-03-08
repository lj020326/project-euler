'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(number):
    for i in xrange(2, (number/2)+1):
        if number % i == 0:
            return False
    return True

primes = []

for i in xrange(2, 150001):
    if is_prime(i):
        primes.append(i)

print primes[10000]
