"""


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


def d(n):
    divisors = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors |= {i, n // i}
    return sum(divisors)


s = 0
num = {n: d(n) for n in range(1, 10000)}
print(num)

for p in num.keys():
    if p == num.get(p, 0):
        s += p
        print(p)

print(s)  # 8659
