__author__ = 'eribeiro'

from math_util import Basic


def n_choose_k(n, k):
    n_fact = Basic.factorial(n)
    nk_fact = Basic.factorial(n - k)
    k_fact = Basic.factorial(k)
    return n_fact // (k_fact * nk_fact)


#TODO: combination


#TODO: permutation
