'''
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(number):
    return str(number) == str(number)[::-1]
    
largest_palindrome = 0    





