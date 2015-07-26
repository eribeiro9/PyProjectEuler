__author__ = 'eribeiro'

from math_util import Algebra


size = 100

square_of_sum = Algebra.square_of_sum(size)
sum_of_squares = Algebra.sum_of_squares(size)

print(square_of_sum - sum_of_squares)
