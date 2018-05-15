"""


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_values = {alphabet[i]: i+1 for i in range(len(alphabet))}

dat = open('p022_names.txt', 'r')
lst = [i.replace('"', '') for i in dat.read().split(',')]
names = sorted(lst)


def alphabetical_value(word):
    return sum([alphabet_values[i] for i in word])


s = 0
for i in range(len(names)):
    s += (i + 1) * alphabetical_value(names[i])

print(s)  # 871198282

dat.close()
