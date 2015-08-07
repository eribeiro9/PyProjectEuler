__author__ = 'eribeiro'

import math
from math_util import Basic, General


# region Factors/Multiples

def is_factor_of(factor, multiple):
    '''
    Return whether factor can divide multiple
    '''
    return multiple % factor == 0


def factors_of(num):
    num_sqrt = math.floor(math.sqrt(num))
    factors = [1]
    add_later = list()
    for factor in range(2, num_sqrt + 1):
        if is_factor_of(factor, num):
            factors.append(factor)
            if factor != num_sqrt:
                add_later.append(num // factor)
    while len(add_later) > 0:
        factors.append(add_later.pop())
    factors.append(num)
    return factors


def num_factors_of(num):
    primes = prime_factors_of(num)
    count_values = General.count_list(primes).values()
    return Basic.product([x + 1 for x in count_values])


def proper_divisors(num):
    factors = factors_of(num)
    factors.pop()
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


def smallest_multiple(limit):
    product_ = Basic.product(range(1, limit + 1))
    primes = primes_under(limit)
    primes_product = Basic.product(primes)
    max_step = product_ // primes_product
    for multiplier in range(1, max_step + 1):
        num = primes_product * multiplier
        for j in range(2, limit + 1):
            if not is_factor_of(j, num):
                break
        else:
            return num
    return product_

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
    for i in range(3, limit, 2):
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


def nth_permutation(n, list_):
    permutation = list()
    num_permutations = Basic.factorial(len(list_))
    n %= num_permutations
    while n > 0:
        permutations_per_index = num_permutations // len(list_)
        index = n // permutations_per_index
        n %= permutations_per_index
        num_permutations = permutations_per_index
        permutation.append(list_.pop(index))
    permutation += list_
    return permutation


def collatz_iterations(num):
    count = 0
    while num > 1:
        even = num % 2 == 0
        if even:
            num //= 2
        else:
            num = 3 * num + 1
        count += 1
    return count
