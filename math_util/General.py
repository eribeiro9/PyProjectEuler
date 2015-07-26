__author__ = 'eribeiro'

import math


def list_digits(num):
    num = math.fabs(num)
    digits = list()
    while num >= 10:
        digits.append(num % 10)
        num /= 10
    digits.append(num)
    digits.reverse()
    return digits


def is_num_palindrome(num):
    digits = list_digits(num)
    digits_reverse = digits
    digits_reverse.reverse()
    return digits == digits_reverse
