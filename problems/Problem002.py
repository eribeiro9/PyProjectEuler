__author__ = 'eribeiro'

from math_util import NumberTheory


fibonacci = NumberTheory.fibonacci_under(4000000, False)

even_fibonacci = list()
for num in fibonacci:
    if NumberTheory.is_factor_of(2, num):
        even_fibonacci.append(num)

sum_ = sum(even_fibonacci)
print(sum_)
