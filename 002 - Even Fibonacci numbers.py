s = 2
n = 0
n1 = 1
n2 = 2

while n < 4000000:
    n = n1 + n2
    n1 = n2
    n2 = n
    n = n1 + n2
    n1 = n2
    n2 = n
    n = n1 + n2
    n1 = n2
    n2 = n
    if n < 4000000:
        s += n
    else:
        print(s)
