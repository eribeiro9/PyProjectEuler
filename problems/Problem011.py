__author__ = 'Eric'

from utilities import CSVReader

data = CSVReader.problem11()
length = 4

max_product = 1

data_length = len(data[0])
data_height = len(data)

for col in range(data_length):
    for row in range(data_height):
        # compare product right, down, diagUpR, diagDownR to max_product
        if col < data_length - length:
            # check right
            y = 0
        x = 3
