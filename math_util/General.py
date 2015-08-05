__author__ = 'eribeiro'


def is_palindrome(num):
    '''
    Returns whether num is a plaindrome
    '''
    return str(num) == str(num)[::-1]


def count_list(list_):
    '''
    Creates a dictionary from counting values in a list
    :param list_: A list of values to be counted
    :return: A dictionary where the keys are the values that appeared in the list
            and whose values are the number of times each value appeared
    '''
    counts = dict()
    while len(list_) > 0:
        item = list_.pop()
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def letter_num(letter):
    '''
    Returns letter's place in the alphabet
    '''
    letter = letter.lower()
    return ord(letter) - ord("a") + 1


def num_digits(num):
    return len(str(num))


def first_digits(num, digits):
    '''
    Returns the first digits digits of num
    '''
    return int(str(num)[0:digits])


def sum_of_digits(num):
    '''
    Returns the sum of the digits of num
    '''
    chars = list(str(num))
    digits = [int(x) for x in chars]
    return sum(digits)


def pretty_int(num):
    '''
    Returns a string version of num with commas as thousand separators
    '''
    triples = list()
    while num >= 1000:
        triple = str(num % 1000)
        while len(triple) < 3:
            triple = "0" + triple
        triples.append(triple)
        num //= 1000
    triples.append(str(num))
    triples.reverse()
    return ",".join(triples)
