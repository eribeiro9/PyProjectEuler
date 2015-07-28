__author__ = 'Eric'

import time
from math_util import Algebra, General, NumberTheory


def solve(problem):
    if problem == 1:
        time_solve(solve001, ([3, 5], 1000))
    elif problem == 2:
        time_solve(solve002, (4000000, False))
    elif problem == 3:
        time_solve(solve003, [600851475143])
    elif problem == 4:
        time_solve(solve004, [1000])
    elif problem == 5:
        time_solve(solve005, [20])
    elif problem == 6:
        time_solve(solve006, [100])
    elif problem == 7:
        time_solve(solve007, [10001])
    elif problem == 8:
        # time_solve(solve008, (read num from site, 13))
        return
    elif problem == 9:
        # solved on paper
        return
    elif problem == 10:
        time_solve(solve010, [2000000])


def time_solve(func, args):
    time.clock()
    result = func(*args)
    time_ = time.clock()
    print("\n" + str(result))
    units = "s"
    if time_ < 0.1:
        time_ *= 1000
        units = "ms"
    print("\n" + "{0:.4f}".format(time_) + units)


# region Problems

def solve001(factors, multiple):
    return NumberTheory.sum_of_multiples_under(factors, multiple)


def solve002(limit, start_with_two_ones):
    fibonacci = NumberTheory.fibonacci_under(limit, start_with_two_ones)
    even_fibonacci = list()
    for num in fibonacci:
        if NumberTheory.is_factor_of(2, num):
            even_fibonacci.append(num)
    return sum(even_fibonacci)


def solve003(limit):
    factors = NumberTheory.prime_factors_of(limit)
    return max(factors)


def solve004(digit_size):
    check_size = digit_size // 10
    checks = range(digit_size - check_size, digit_size)
    mult_table = Algebra.multiplication_table(checks, checks)
    palindromes = list()
    for row in mult_table:
        for num in row:
            if General.is_palindrome(num):
                palindromes.append(num)
    return max(palindromes)


def solve005(limit):
    return Algebra.smallest_multiple(limit)


def solve006(size):
    square_of_sum = Algebra.square_of_sum(size)
    sum_of_squares = Algebra.sum_of_squares(size)
    return square_of_sum - sum_of_squares


def solve007(limit):
    return max(NumberTheory.first_primes(limit))


def solve008(num, length):
    digits = [int(i) for i in list(num)]
    max_product = 1
    for i in range(len(num) - length + 1):
        product = Algebra.product(digits[i:i + length])
        if product > max_product:
            max_product = product
    return max_product


def solve010(limit):
    primes = NumberTheory.primes_under(limit)
    return sum(primes)

# endregion
