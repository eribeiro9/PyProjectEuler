__author__ = 'Eric'

import csv
import Constants


data_files_path = Constants.HOME_DIR + Constants.DATA_FILES_DIR


def load_csv(file, as_int=False):
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

# endregion
