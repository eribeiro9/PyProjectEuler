__author__ = 'eribeiro'

from math_util import General, Algebra


digit_size = 100
check_size = digit_size / 10

checks = range(digit_size - check_size, digit_size)

mult_table = Algebra.multiplication_table(checks, checks)

palindromes = list()
# populate palindromes from mult_table

print(max(palindromes))
