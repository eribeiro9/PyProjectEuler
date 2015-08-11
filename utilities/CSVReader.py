__author__ = 'Eric'

import csv
import Constants


data_files_path = Constants.HOME_DIR + Constants.DATA_FILES_DIR


def load_csv(file, as_int=False):
    '''
    Reads a .csv file and returns the data as a 2D list
    :param file: Name of .csv file to read
    :param as_int: If the data is int or string
    :return: 2D list of data
    '''
    rt_data = list()
    path = data_files_path + file
    with open(path, newline='') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            rt_data.append(row)
    if as_int:
        rt_data = [[int(x) for x in row] for row in rt_data]
    return rt_data


# region Problems

def problem8():
    data = load_csv("problem008.csv")
    return data[0][0]


def problem11():
    data = load_csv("problem011.csv", True)
    return data


def problem13():
    data = load_csv("problem013.csv", True)
    return data[0]


def problem18():
    data = load_csv("problem018.csv", True)
    return data


def problem22():
    data = load_csv("problem022.csv")
    return data[0]


def problem67():
    data = load_csv("problem067.csv", True)
    return data


def number_words():
    data = load_csv("number-words.csv")
    return data[0]

# endregion
