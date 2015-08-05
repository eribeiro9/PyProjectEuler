__author__ = 'eribeiro'


#TODO: determinant
# def determinant(matrix):


def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return
    product = [v1 * v2 for v1, v2 in zip(vector1, vector2)]
    return sum(product)


#TODO: cross product
