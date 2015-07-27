__author__ = 'eribeiro'

from math_util import NumberTheory


limit = 10001

prime = max(NumberTheory.first_primes(limit))

print(prime)
