__author__ = 'eribeiro'

import math


# region Factors/Multiples

def is_factor_of(factor, multiple):
    return multiple % factor == 0


def factors_of(num):
    factors = list()
    for factor in range(1, num + 1):
        if is_factor_of(factor, num):
            factors.append(factor)
    return factors


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

# endregion


# region Fibonacci

def fibonacci_under(limit, starts_with_two_ones=True):
    fibonacci = ([1, 2], [1, 1])[starts_with_two_ones]
    next_num = fibonacci[-1] + fibonacci[-2]
    while next_num <= limit:
        fibonacci.append(next_num)
        next_num = fibonacci[-1] + fibonacci[-2]
    return fibonacci


def first_fibonacci(limit, starts_with_two_ones=True):
    fibonacci = ([1, 2], [1, 1])[starts_with_two_ones]
    next_num = fibonacci[-1] + fibonacci[-2]
    while len(fibonacci) <= limit:
        fibonacci.append(next_num)
        next_num = fibonacci[-1] + fibonacci[-2]
    return fibonacci

# endregion


# region Primes

def primes_under(limit):
    # TODO: efficiency
    if limit <= 2:
        return list()
    primes = [2]
    for i in range(3, limit):
        add = True
        i_sqrt = math.sqrt(i)
        for prime in primes:
            if prime > i_sqrt:
                break
            elif is_factor_of(prime, i):
                add = False
                break
        if add:
            primes.append(i)
    return primes


def first_primes(limit):
    # TODO: efficiency
    primes = [2]
    if limit < 1:
        return list()
    elif limit == 1:
        return primes
    i = 3
    while len(primes) < limit:
        add = True
        i_sqrt = math.floor(math.sqrt(i))
        for prime in primes:
            if prime > i_sqrt:
                break
            elif is_factor_of(prime, i):
                add = False
                break
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
            num //= choice
            if num == 1:
                return factors
    if num > 1:
        factors.append(num)
    return factors

# endregion
