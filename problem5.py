'''
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?


# We don't have to consider odd numbers. And the will be surely greater than 2520.
# We can skip the numbers from 1 to 10 checking because a number divisible by 20
# surely divisible by 10, number divisible by 18 surely divisible by 9, and so on.

domain = []

for i in xrange(2, 240000001, 2):
    domain.append(i)

p_list = []
flag = True        
for number in domain:
    for i in xrange(11, 21):
        if number % i != 0:
            flag = False
            break
    if not flag:
        flag = True
    else:
        p_list.append(number)
        
print min(p_list)
'''
# long but very efficient method. It completes execution in 0.008s (usertime).

# Let N be the smallest number that is divisible by all the integers from 2 to k.
# For N to be the smallest value with this property we must ensure that in its
# prime factorisation it does not contain any more prime factors than is
# absolutely necessary.
# Applying this principle for case k = 20
# N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560
      
def is_prime(n):
    for i in xrange(2, (n/2)+1):
        if n % i == 0:
            return False
    return True
    


def prime_factors(number):
    prime_factor_list = []
    if is_prime(number):
        prime_factor_list.append(number)
    else:
        for i in xrange(2, (number/2)+1):
            if is_prime(i) and number % i == 0:
                prime_factor_list.append(i)
    return prime_factor_list

def s_prime_factors(n):
    s_prime_factors_list = []
    if n == 8:
        for x in xrange(3):
            s_prime_factors_list.append(2)
    elif n == 16:
        for x in xrange(4):
            s_prime_factors_list.append(2)
    elif n == 18:
        for x in xrange(1):
            s_prime_factors_list.append(2)
        for x in xrange(2):
            s_prime_factors_list.append(3)
    else:
        number = 1
        for x in prime_factors(n):
            number *= x
            s_prime_factors_list.append(x)
        if number > n:
            for x in prime_factors(n):
                number /= x
                if number == n:
                    del(s_prime_factors_list[s_prime_factors_list.index(x)])
                    break
        elif number < n:
            for x in prime_factors(n):
                number *= x
                if number == n:
                    s_prime_factors_list.append(x)
                    break
    return s_prime_factors_list
    


final_list = []
for x in xrange(2, 21):
    n = s_prime_factors(x)
    for factor in n:
        if factor not in final_list:
            final_list.append(factor)
        else:
            if n.count(factor) > final_list.count(factor):
                final_list.append(factor)                    
        
minimum_product = 1
for factor in final_list:
    minimum_product *= factor

print minimum_product

    
     
    
            
                    
                
        
    

        
        

