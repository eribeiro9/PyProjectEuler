__author__ = 'Eric'

from timeit import default_timer as timer
from math_util import Basic, General, NumberTheory, Statistics
from utilities import CSVReader  # , PrettyPrint


def solve(problem, spoilers=True, print_=True):
    '''
    Solves problem and times how long to get result
    :param problem: Number of Project Euler problem to solve (1+)
    :param spoilers: True to display answer to problem, False otherwise
    :param print_: True to print result (if spoilers) and time taken
    :return: Tuple containing problem number, result (if spoilers), and time taken to solve problem
    '''
    (result, time_) = time_solve(solve_args[problem][0], solve_args[problem][1])
    if print_:
        if spoilers:
            print(problem, result, "{0:.4f}".format(time_) + "ms", sep="        ")
        else:
            print(problem, "{0:.4f}".format(time_) + "ms", sep="        ")
    if spoilers:
        return problem, result, time_
    return problem, time_


def solve_all(spoilers=True):
    '''
    Solves all problems in the solve_args dictionary and prints answers (depending on spoilers),
    and time taken to solve each (in ms)
    :param spoilers: True to display answer to problems, False otherwise
    '''
    problems = list(solve_args)
    results = list()
    for problem in problems:
        results.append(solve(problem, spoilers))
    # TODO: PrettyPrint.print_table(results)


def time_solve(func, args):
    '''
    Times how long it takes to run func using args in milliseconds
    :param func: Function to run
    :param args: Arguments to send func
    :return: Return value from func and time taken to run (in ms)
    '''
    start = timer()
    result = func(*args)
    end = timer()
    return result, (end - start) * 1000  # Return time in ms


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
    square_of_sum = Basic.square_of_sum_up_to(size)
    sum_of_squares = Basic.sum_of_squares_up_to(size)
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
    # TODO: Solve according to where 1000 is the variable
    return 31875000


def solve010(limit):
    primes = NumberTheory.primes_under(limit)
    return sum(primes)


def solve011(data, length):
    return General.max_product_of(data, length)


def solve012(limit):
    num = 2
    while NumberTheory.num_factors_of(Basic.sum_up_to(num)) <= limit:
        num += 1
    return Basic.sum_up_to(num)


def solve013(nums, digits):
    return General.first_digits(sum(nums), digits)


def solve014(limit):
    iterations = NumberTheory.collatz_iterations_under(limit)
    return General.key_with_max_value(iterations)


def solve015(size):
    return Statistics.n_choose_k(size * 2, size)


def solve016(exponent):
    num = 2 ** exponent
    return General.sum_of_digits(num)


def solve017(words, limit):
    num_words = str()
    for i in range(1, limit):
        num_words += General.num_as_word(i, words).replace(" ", "")
    return len(num_words)


def solve018(triangle):
    start = triangle.pop()
    return General.max_two_lower(start, triangle)


def solve020(num):
    factorial = Basic.factorial(num)
    return General.sum_of_digits(factorial)


def solve021(num):
    divisors = NumberTheory.proper_divisors(num)
    return sum(divisors)


def solve022(names):
    names.sort()
    sum_ = 0
    for i in range(len(names)):
        name = names[i]
        name_score = [General.letter_num(letter) for letter in name]
        sum_ += sum(name_score) * (i + 1)
    return sum_


def solve024(n):
    list_ = list(range(10))
    permutation = NumberTheory.nth_permutation(n, list_)
    permutation = [str(x) for x in permutation]
    return "".join(permutation)


def solve025(digits):
    fibonacci = [1, 1]
    while General.num_digits(fibonacci[-1]) < digits:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return len(fibonacci)


def solve028(size):
    length = size // 2
    sum_ = 1  # The center 1 starts counted
    pos = [1, 1, 1, 1]
    vel = [2, 4, 6, 8]
    accl = 8
    for i in range(length):
        pos = [p + v for p, v in zip(pos, vel)]
        vel = [v + accl for v in vel]
        sum_ += sum(pos)
    return sum_


def solve067(triangle):
    start = triangle.pop()
    return General.max_two_lower(start, triangle)

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
    11: (solve011, [CSVReader.problem11(), 4]),
    12: (solve012, [500]),
    13: (solve013, [CSVReader.problem13(), 10]),
    14: (solve014, [1000000]),
    15: (solve015, [20]),
    16: (solve016, [1000]),
    # 17: (solve017, [CSVReader.number_words(), 1000]),  # FIXME: WRONG
    18: (solve018, [CSVReader.problem18()]),
    # 19: (solve019, list()),
    20: (solve020, [100]),
    # 21: (solve021, [10000]),  # FIXME: WRONG
    22: (solve022, [CSVReader.problem22()]),
    # 23: (solve023, list()),
    # 24: (solve024, [1000000]),  # FIXME: WRONG
    25: (solve025, [1000]),
    # 26: (solve026, [1000]),
    # 27: (solve027, list()),
    28: (solve028, [1001]),
    # 29: (solve029, [100])
    67: (solve067, [CSVReader.problem67()])
}
