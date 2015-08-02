__author__ = 'Eric'

from timeit import default_timer as timer
from math_util import Basic, General, NumberTheory
from utilities import CSVReader


def solve(problem, spoilers=True):
    (result, time_) = time_solve(solve_args[problem][0], solve_args[problem][1])
    if spoilers:
        print(problem, result, "{0:.4f}".format(time_) + "ms", sep="        ")
    else:
        print(problem, "{0:.4f}".format(time_) + "ms", sep="        ")


def solve_all(spoilers=True):
    problems = list(solve_args)
    for problem in problems:
        solve(problem, spoilers)


def time_solve(func, args):
    start = timer()
    result = func(*args)
    end = timer()
    return result, (end - start) * 1000


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
    mult_table = Basic.multiplication_table(checks, checks)
    palindromes = list()
    for row in mult_table:
        for num in row:
            if General.is_palindrome(num):
                palindromes.append(num)
    return max(palindromes)


def solve005(limit):
    return NumberTheory.smallest_multiple(limit)


def solve006(size):
    square_of_sum = Basic.square_of_sum(size)
    sum_of_squares = Basic.sum_of_squares(size)
    return square_of_sum - sum_of_squares


def solve007(limit):
    return max(NumberTheory.first_primes(limit))


def solve008(num, length):
    digits = [int(i) for i in list(num)]
    max_product = 1
    for i in range(len(num) - length + 1):
        product = Basic.product(digits[i:i + length])
        if product > max_product:
            max_product = product
    return max_product


def solve009():
    # Solved on paper
    # TODO: Write solution
    return 31875000


def solve010(limit):
    primes = NumberTheory.primes_under(limit)
    return sum(primes)


def solve012(limit):
    num = 2
    while NumberTheory.num_factors_of(Basic.sum_up_to(num)) <= limit:
        num += 1
    return Basic.sum_up_to(num)


def solve013(nums, digits):
    return General.first_digits(sum(nums), digits)

# endregion


solve_args = {
    1: (solve001, [[3, 5], 1000]),
    2: (solve002, [4000000, False]),
    3: (solve003, [600851475143]),
    4: (solve004, [1000]),
    5: (solve005, [20]),
    6: (solve006, [100]),
    7: (solve007, [10001]),
    8: (solve008, [CSVReader.problem8(), 13]),
    9: (solve009, list()),
    10: (solve010, [2000000]),
    # 11: (solve011, [CSVReader.problem11(), 4]),
    12: (solve012, [500]),
    13: (solve013, [CSVReader.problem13(), 10])
}
