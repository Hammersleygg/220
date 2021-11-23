"""
Name: Gavin Hammersley
lab12.py

Problem: use while loops to create a number guessing game

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    val_list = []
    file = open(filename, "r")
    line = file.readline()
    while line != '':
        split_line = line.split()
        count = 0
        while count < len(split_line):
            val_list.append(eval(split_line[count]))
            count += 1
        line = file.readline()
    return val_list


def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if search_val == values[count]:
            return True
        count += 1
        # print(count)
    return False


def main():
    print(read_data("read_data_test_data.txt"))
    # print(is_in_linear(45, read_data("read_data_test_data.txt")))


main()
