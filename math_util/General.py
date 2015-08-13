__author__ = 'eribeiro'


def is_palindrome(num):
    '''Returns whether num is a plaindrome'''
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
    '''Returns letter's place in the alphabet'''
    letter = letter.lower()
    return ord(letter) - ord("a") + 1


def num_digits(num):
    '''Returns the number of digits of num'''
    return len(str(num))


def first_digits(num, digits):
    '''Returns the first digits digits of num'''
    return int(str(num)[0:digits])


def sum_of_digits(num):
    '''Returns the sum of the digits of num'''
    chars = list(str(num))
    digits = [int(x) for x in chars]
    return sum(digits)


def num_to_triples(num):
    triples = list()
    while num >= 1000:
        triple = str(num % 1000)
        while len(triple) < 3:
            triple = "0" + triple
        triples.append(triple)
        num //= 1000
    triples.append(str(num))
    triples.reverse()
    return triples


def pretty_int(num):
    '''Returns a string version of num with commas as thousand separators'''
    return ",".join(num_to_triples(num))


def key_with_max_value(dict_):
    '''Returns key from dictionary whose value is maximum'''
    keys = list(dict_.keys())
    values = list(dict_.values())
    return keys[values.index(max(values))]


def max_two_lower(old_sums, triangle):
    '''
    Adds each point in the last row of triangle to the greater of the two sums "below" it
    :param old_sums: List of numerics
    :param triangle: 2D list of numeric data points
    :return: A list of numerics whose size is one less than old_sums
    '''
    if len(triangle) <= 1 or len(old_sums) <= 2:
        return triangle[0][0] + max(old_sums)
    new_sums = list()
    for i in range(len(old_sums) - 1):
        new_sums.append(triangle[-1][i] + max(old_sums[i:i+2]))
    triangle.pop()
    return max_two_lower(new_sums, triangle)


def num_as_word(num, words):
    '''Returns the number in word form (ie num_as_word(21) = twenty one)'''
    num_word = str()
    if num <= 20:
        return words[num]
    elif num < 100:
        num_word += words[num // 10 + 18]
        if num % 10 != 0:
            num_word += " " + words[num % 10]
        return num_word
    elif num < 1000:
        num_word += words[num // 100]
        num_word += " " + words[28]
        if num % 100:
            num_word += " and "
            num_word += num_as_word(num % 100, words)
    else:
        return "Number not supported"
    return num_word


def max_product_of(data, length):
    max_product = 1
    data_length = len(data[0])
    data_height = len(data)
    for col in range(data_length):
        for row in range(data_height):
            products = [1, 1, 1, 1]
            if col <= data_length - length:
                for i in range(length):
                    products[0] *= data[row][col + i]
            if row <= data_height - length:
                for i in range(length):
                    products[1] *= data[row + i][col]
            if col <= data_length - length and row >= length - 1:
                for i in range(length):
                    products[2] *= data[row - i][col + i]
            if col <= data_length - length and row <= data_height - length:
                for i in range(length):
                    products[3] *= data[row + i][col + i]
            max_product = max(max_product, max(products))
    return max_product
