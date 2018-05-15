"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

numbers_as_written = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}


def number_of_letters(num):
    if num <= 10:
        return numbers_as_written[num]
    elif num < 100:
        if num // 10 == 1:
            return numbers_as_written[num]
        elif num % 10 == 0:
            return numbers_as_written[num]
        else:
            return number_of_letters((num // 10) * 10) + number_of_letters(num % 10)
    else:
        if num % 100 == 0:
            return number_of_letters(num // 100) + 7
        else:
            return number_of_letters(num // 100) + 7 + 3 + number_of_letters(num % 100)


s = 11
for i in range(1, 1000):
    s += number_of_letters(i)

print(s)  # 21124
