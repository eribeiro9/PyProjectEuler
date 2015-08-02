__author__ = 'eribeiro'


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def count_list(list_):
    counts = dict()
    while len(list_) > 0:
        item = list_.pop()
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def first_digits(num, digits):
    while num >= 10 ** digits:
        num //= 10
    return num


def pretty_int(num):
    triples = list()
    while num > 1000:
        # FIXME: Leading zeros break triples
        triples.append(str(num % 1000))
        num //= 1000
    triples.append(str(num))
    triples.reverse()
    return ",".join(triples)
