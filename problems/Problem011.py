__author__ = 'Eric'

from utilities import CSVReader

data = CSVReader.problem11()
length = 4

max_product = 1

for col in range(len(data[0])):
    for row in range(len(data)):
        # compare product right, down, diagUpR, diagDownR to max_product
        x = 3
