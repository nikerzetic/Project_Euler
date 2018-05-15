# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

pol = []

for n1 in range(900, 1000):
    for n2 in range(900, 1000):
        nprod = n1 * n2
        prod = str(nprod)
        a = prod[0]
        b = prod[len(prod) - 1]
        c = prod[1]
        d = prod[len(prod) - 2]
        e = prod[2]
        f = prod[len(prod) - 3]
        if a == b and c == d and e == f:
                pol.append(nprod)

print(max(pol), pol)

for i in range(len(prod)):
    print(prod[i])
