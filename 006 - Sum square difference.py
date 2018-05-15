from math import factorial

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
sqs = 2

for i in range(1, 101):
    sqs *= factorial(100)/i

print(sqs)
"""

sum1 = 0
for i in range(1, 101):
    sum1 += i

sum2 = 0
for i in range(1, 101):
    sum2 += i**2

sol = sum1 ** 2 - sum2
print(sum1, sum2, sol)

"""
Tuja resitev
n = 100
sum1 = n**2 * (n+1)**2 /4
sum2 = n * (n+1) * (2*n +1) /6
sol = sum1 - sum2
"""
