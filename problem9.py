'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

triplets = [(a, b, c) for a in xrange(1, 4000000) for b in xrange(a, 4000000) for c in xrange(b, 4000000)
    if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000]

print triplets[0][0] * triplets[0][1] * triplets[0][2]


