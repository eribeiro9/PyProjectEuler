__author__ = 'eribeiro'

from math_util import NumberTheory

limit = 125 #9 seconds for 125

num = 0
add = 1

while len(NumberTheory.factors_of(num)) < limit:
    num += add
    add += 1

print(num)
