"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return 1 + dolzina_zaporedja(naslednji_clen(n))


def najdaljse_zaporedje(m,n):
    najdalzap = 0
    zacetni_clen = 0
    for i in range(m, n + 1):
        dz = dolzina_zaporedja(i)
        if dz > najdalzap:
            najdalzap, zacetni_clen = dz, i
    return zacetni_clen


print(najdaljse_zaporedje(3, 1000000))
