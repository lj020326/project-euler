'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(number):
    for i in xrange(2, (number/2)+1):
        if number % i == 0:
            return False
    return True
    
def sum_prime(number):
    s = 2
    for i in xrange(3, number, 2):
        if is_prime(i):
            s += i
    return s
    
print sum_prime(2000000)        
    
