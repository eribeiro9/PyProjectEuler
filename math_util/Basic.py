__author__ = 'eribeiro'

from functools import reduce
from operator import mul


# region Sum

def sum_of_squares(limit):
    return sum([x ** 2 for x in range(1, limit + 1)])


def square_of_sum(limit):
    return sum(range(1, limit + 1)) ** 2


def sum_up_to(limit):
    return limit * (limit + 1) // 2

# endregion


def product(list_):
    return reduce(mul, list_)


def multiplication_table(list1, list2):
    mult_table = list()
    for l1 in list1:
        next_row = list()
        for l2 in list2:
            next_row.append(l1 * l2)
        mult_table.append(next_row)
    return mult_table
