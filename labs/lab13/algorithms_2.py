"""
Name: Gavin Hammersley
algorithms_2.py

Problem: use binary searching and sorting

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


def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return middle
        if search_val < middle_value:
            right = middle - 1
        if search_val > middle_value:
            left = middle + 1
    return False


def selection_sort(values):
    for i in values:
        if i > (i + 1):
            new = i.replace((i + 1))
            print(new)


def calc_area(rect):
    dx = (rect.getP1().getX() - rect.getP2().getX())
    dy = (rect.getP1().getY() - rect.getP2().getY())

    length = dx
    width = dy
    area = length * width

    return area


def rect_sort(rectangles):

    for rectangle in rectangles:
        if calc_area(rectangle) > calc_area(rectangle + 1):
            new = rectangle.replace(rectangle + 1)
            print(new)


def main():
    # print(read_data("read_data_test_data.txt"))
    # print(is_in_linear(45, read_data("read_data_test_data.txt")))
    # is_in_binary(3, [20, 40, 6, 2, 3, 70])
    selection_sort([5, 3, 4, 2, 1])


main()
