'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(number):
    for i in xrange(2, (number/2)+1):
        if number % i == 0:
            return False
    return True

def prime_factors(number):
    limit = number ** (1 / 2)
    factors_list = []
    for i in xrange(limit, number / 2):
        if is_prime(i) and number % i == 0:
            factors_list.append(i)
    return factors_list
    
print prime_factors(600851475143)