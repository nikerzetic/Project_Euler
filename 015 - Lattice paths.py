"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""


def can_go_right(x):
    return x > 0


def can_go_down(y):
    return y > 0


def number_of_routes(x, y):
    if can_go_right(x) and can_go_down(y):
        print('RD')
        return number_of_routes(x - 1, y) + number_of_routes(x, y - 1)
    elif can_go_right(x):
        print('R')
        return number_of_routes(x - 1, y)
    elif can_go_down(y):
        print('D')
        return number_of_routes(x, y - 1)
    else:
        print('Finish')
        return 1


number_of_routes(20, 20)
