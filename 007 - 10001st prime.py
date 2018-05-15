import time, math

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
ps = []


for p in range(1, 130000):
    c = 0
    for n in range(2, p):
        if p % n == 0:
            c += 1
    if c == 0:
        ps.append(p)
        print(p)

print("Solution:", ps[10002])
"""


# Tuja resitev:

s = time.time()
def IsPrime(n):
	if n == 2:
		return 1
	elif n % 2 == 0:
		return 0

i = 3
range1 = int(math.sqrt(n)) + 1
while( i < range1):
	if(n % i == 0):
		return 0
	i += 1
return 1

N,T = 1,3
while N < 10001:
	if IsPrime(T):
		N+=1
	T+=2
print(T-2)
print(time.time() - s)
