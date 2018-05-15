"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

dat = open("p067_triangle.txt", "r")
lst = dat.readlines()

tri = []
for i in range(len(lst)):
    line = lst[i][:-1]
    if i > 0:
        line = line.split(" ")
        new = []
        for k in range(len(line)):
            new.append(int(line[k]))
        tri.append(new)
    else:
        n = int(lst[0])
        tri.append([n])

while len(tri) > 1:
    # vsakemu elementu predzadnje vrstice pristeje vecjega izmed spodnjih dveh elementov
    for i in range(len(tri[-2])):
        tri[-2][i] += max(tri[-1][i], tri[-1][i+1])
    del(tri[-1])

print(tri[0][0])  # 7273

dat.close()
