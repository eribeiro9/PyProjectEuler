__author__ = 'eribeiro'

import math


def is_factor_of(factor, multiple):
    return multiple % factor == 0


def fibonacci_under(limit, starts_with_two_ones=True):
    fibonacci = ([1, 2], [1, 1])[starts_with_two_ones]
    next_num = fibonacci[-1] + fibonacci[-2]
    while next_num <= limit:
        fibonacci.append(next_num)
        next_num = fibonacci[-1] + fibonacci[-2]
    return fibonacci


def primes_under(limit):
    # TODO: efficiency, efficiency, efficiency
    if limit <= 2:
        return list()
    primes = [2]
    i = 3
    while i < limit:
        add = True
        i_sqrt = math.floor(math.sqrt(i))
        for prime in primes:
            if prime <= i_sqrt and is_factor_of(prime, i):
                add = False
        if add:
            primes.append(i)
        i += 1
    return primes


def prime_factors_of(num):
    factors = list()
    num_sqrt = math.floor(math.sqrt(num))
    choices = [2]
    choices.extend(range(3, num_sqrt, 2))
    for choice in choices:
        while is_factor_of(choice, num):
            factors.append(choice)
            num /= choice
            if num == 1:
                return factors
    return ([num], factors)[len(factors) > 0]


def sum_of_multiples_under(factors, limit):
    sum_ = 0
    for multiple in range(1, limit):
        add = False
        for factor in factors:
            if is_factor_of(factor, multiple):
                add = True
        if add:
            sum_ += multiple
    return sum_
