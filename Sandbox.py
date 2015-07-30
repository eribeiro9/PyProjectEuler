
from problems import Problems
from utilities import CSVReader
from math_util import Algebra, NumberTheory


#Problems.solve_all()
#data = CSVReader.load_csv("problem011.csv")

#test = data[0]
#test = [int(x) for x in test]

#print(str(Algebra.product(NumberTheory.first_primes(225))))

result, time_ = Problems.time_solve(NumberTheory.primes_under, [3000000])
print(time_)