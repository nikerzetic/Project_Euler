"""


A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solution:

0: 9! = 362 880
1: 9! = 362 880
---------------
725 760

=> 2 _ _ _ _ _ _ _ _ _ _

20: 8! = 40 320
21: 8! = 40 320
23:
24
25
26: 8! = 40 320
---------------
32320

260: 5040
261
263
264
265
267
----------------
2080

2671:
---
640

26710
26713
26714
26715
26718
---
40

267180
---
16

2671803
2671804
---
4 to one million

267418043
---
2

=> 26741804593

"""
import math

num = range(1, 10)
r = 1000000
n = ''
fac = range(9, 1)

for i in fac:
    j = 0
    f = math.factorial(i)
    while r - f > 0:
        r -= f
        j += 1
    n += str(num[j])
    num = num[:j] + num[j+1:]

print('Solution: ', n)
