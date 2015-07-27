__author__ = 'eribeiro'

from math_util import General, Algebra


digit_size = 1000
check_size = digit_size // 10
checks = range(digit_size - check_size, digit_size)

mult_table = Algebra.multiplication_table(checks, checks)

palindromes = list()
for row in mult_table:
    for num in row:
        if General.is_palindrome(num):
            palindromes.append(num)

print(max(palindromes))
