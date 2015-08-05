__author__ = 'eribeiro'

from functools import reduce
from operator import mul


# region Sum

def sum_of_squares(list_):
    return sum([x ** 2 for x in list_])


def sum_of_squares_up_to(limit):
    return sum_of_squares(range(1, limit + 1))


def square_of_sum(list_):
    return sum(list_) ** 2


def square_of_sum_up_to(limit):
    return sum_up_to(limit) ** 2


def sum_up_to(limit):
    '''
    Finds the sum of all the natural numbers up to (and including) limit
    '''
    return limit * (limit + 1) // 2

# endregion


def product(list_):
    '''
    Multiplies all values in a list together
    '''
    return reduce(mul, list_)


def factorial(num):
    '''
    Returns num! (num * (num - 1) * ... * 2 * 1)
    '''
    return product(range(1, num + 1))


def multiplication_table(list1, list2):
    '''
    Creates a 2D list "multiplication table"
    :param list1: The values on the top of the table
    :param list2: The values on the left of the table
    :return: The multiplication table as a 2D list of numerics
    '''
    return [[l1 * l2 for l1 in list1] for l2 in list2]
