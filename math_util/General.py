__author__ = 'eribeiro'


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def count_list(list_):
    item_count = list()
    for item in list_:
        if item not in item_count:
            item_count.append((item, 1))
        else:
            item_count
        # add item to item_count
