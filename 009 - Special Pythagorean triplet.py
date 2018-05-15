import math

"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Se dobro, da nisi reseval, kar naloga zahteva.
for i in range(1, 31):
    s1 = 0
    p1 = 1
    s1 += i**2
    p1 *= i
    for j in range(i + 1, 31):
        s2 = 0
        p2 = 1
        s2 += j**2 + s1
        p2 *= j * p1
        if s2 <= 1000:
            for k in range(j + 1, 31):
                s3 = 0
                p3 = 1
                s3 += k**2 + s2
                p3 *= k * p2
                if s3 == 1000:
                    print(p3, i, j, k)
"""

for i in range(1, 500):
    s1 = float(i**2)
    for j in range(i, 500):
        s2 = float(s1 + j**2)
        if math.sqrt(s2) % 1 == 0:
            # print(i, j, s2, " ", i + j + math.sqrt(s2))   # ta vrstica je odvec
            if i + j + math.sqrt(s2) == 1000:
                print("-->", i*j*math.sqrt(s2))
