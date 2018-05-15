"""


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
num_of_days = {"jan": 31, "feb": 28, "mar": 31, "apr": 30, "may": 31, "jun": 30, "jul": 31, "aug": 31, "sep": 30, "oct": 31, "nov": 30, "dec": 31}
months = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun', 7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'}
days_of_week = {1: "mon", 2: "tue", 3: "wed", 4: "thu", 5: "fri", 6: "sat", 7: "sun"}


class Day:

    def __init__(self, day, month, year_o, name):
        self.day = day
        self.month = month
        self.year_o = year_o
        self.name = name

    def __str__(self):
        return '%s.%s.%s - %s' % (self.day, self.month, self.year_o, days_of_week[self.name])

    def next_day(self):
        # naslednji dan
        if self.name == 7:
            self.name = 1
        else:
            self.name += 1

        if self.day == 31 and self.month == 12:
            self.year_o += 1
            self.day, self.month = 1, 1
        elif is_leap_year(self.year_o) and self.month == 2:
            if self.day == 29:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        else:
            if self.day == num_of_days[months[self.month]]:
                self.day = 1
                self.month += 1
            else:
                self.day += 1


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


current = Day(1, 1, 1900, 1)
while current.year_o < 1901:
    current.next_day()

counter = 0
while current.year_o < 2001:
    # je nedeljeva prvi dan v mesecu
    if current.day == 1 and current.name == 7:
        counter += 1
        print(current)

    # naslednji dan
    current.next_day()

print(counter)  # 171
