__author__ = 'eribeiro'

from math_util import NumberTheory


limit = 2000000

primes = NumberTheory.primes_under(limit)

print(sum(primes))
