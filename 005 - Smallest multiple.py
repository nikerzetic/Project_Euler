#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#first let's do this the smart way
gs = 11 * 13 * 2 * 17 * 19 * 2520
print(gs)

#and then the hard way
prs = []
nps = []
fts = [2]
for n1 in range(2, 21):
    p = 0
    for p1 in range(2, n1):
        if n1 % p1 == 0:
            p += 1
    if p == 0:
        prs.append(n1)
    else:
        nps.append(n1)

for n2 in nps:
    while n2 != 1:
        for p2 in fts:
            if n2 % p2 == 0:
                n2 //= p2
        for p2 in prs:
            while n2 % p2 == 0 and n2 != 1:
                fts.append(p2)
                n2 //= p2

for p3 in prs:
    if p3 not in fts:
        fts.append(p3)

pro = 1

for n4 in fts:
    pro *= n4


print(prs, nps, fts)
print(pro)
