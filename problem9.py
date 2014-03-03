#special pythagorean triplet

for x in [a * b * c for a in range(450) for b in range(450) for c in range(450) if ((a < b < c) and (a**2 + b**2 == c **2) and (a + b + c == 1000)) ]:
	print x
