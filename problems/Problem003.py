__author__ = 'eribeiro'

from math_util import NumberTheory


limit = 600851475143

factors = NumberTheory.prime_factors_of(limit)
print(max(factors))
