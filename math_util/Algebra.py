__author__ = 'eribeiro'

from functools import reduce
from math_util import NumberTheory


def sum_of_squares(limit):
    return sum([x ** 2 for x in range(1, limit + 1)])


def square_of_sum(limit):
    return sum(range(1, limit + 1)) ** 2


def product(list_):
    return reduce(lambda x, y: x * y, list_)


def product_up_to(limit):
    return limit * (limit + 1) / 2 # TODO: WRONG


def smallest_multiple(limit):
    product_ = product(range(1, limit + 1))
    primes = NumberTheory.primes_under(limit)
    primes_product = product(primes)
    max_step = product_ // primes_product
    for multiplier in range(1, max_step + 1):
        num = primes_product * multiplier
        for j in range(2, limit + 1):
            if not NumberTheory.is_factor_of(j, num):
                break
        else:
            return num
    return product_


def multiplication_table(list1, list2):
    mult_table = list()
    for l1 in list1:
        next_row = list()
        for l2 in list2:
            next_row.append(l1 * l2)
        mult_table.append(next_row)
    return mult_table
