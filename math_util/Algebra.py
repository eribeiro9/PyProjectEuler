__author__ = 'eribeiro'


def sum_of_squares(limit):
    return sum([x ** 2 for x in range(1, limit + 1)])


def square_of_sum(limit):
    return sum(range(1, limit + 1)) ** 2


def multiplication_table(list1, list2):
    mult_table = list()
    for l1 in list1:
        next_row = list()
        for l2 in list2:
            next_row.append(l1 * l2)
        mult_table.append(next_row)
    return mult_table
