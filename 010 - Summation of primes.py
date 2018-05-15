"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

"""
# Zelo neucinkovita resitev - potrebuje kakih 30 min racunanja
s = 2
p = [2]

for i in range(3, 2000000, 2):
    print("<@>", i)
    x = 0
    for j in p:
        if i % j == 0:
            x += 1
    if x == 0:
        s += i
        p.append(i)

print(s)
"""

"""
# vsote zaporednih prastevil pod 100

p = []

for i in range(2, 100):
    x = 0
    for j in range(2, i):
        if i % j == 0:
                x += 1
    if x == 0:
        p.append(i)

for i in range(len(p)):
    lst = []
    for j in range(i):
        lst.append(p[j])
    solst = sum(lst)
    x = 0
    for k in range(2, solst):
        if solst % k == 0:
            x += 1
    if x != 0:
        print("(", i, ") ", lst, " = ", solst)
    else:
        print("(", i, ") ", lst, " = ", solst, " <-- ")
"""

# s pomocjo nacina s spleta

N = 2000000

is_prime = [1 for num in range(N)]
is_prime[0] = 0
is_prime[1] = 0


def set_prime(num):
    for x in range(num*2, N, num):
        is_prime[x] = 0


for num in range(N):
    if is_prime[num] == 1:
        set_prime(num)

primes = [num for num in range(N) if is_prime[num] == 1]

print(sum(primes))
