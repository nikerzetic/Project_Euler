factors = []
n1 = 600851475143

#n = 10000000


for n2 in range(2, n1):
    if n1 == 1:
        break
    while n1 % n2 == 0:
        n1 //= n2
        factors.append(n2)


print(factors)
print(max(factors))

#someone else's solution
def delbart(t,n):
    if n > 0:
        if not (t%n):
            if delbart(t, n-1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

i = 20
while not delbart(i,20):
    i +=20

print(i)
