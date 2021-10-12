"""
Name: Gavin Hammersley
lab7.py

Problem: working with strings

Partner: <your partner's name goes here – first and last>
"""
# import math


def cash_conversion():
    integer = input("Enter your integer here: ")
    formatted_integer = "{:.2f}".format(int(integer))
    print(formatted_integer)


def encode():
    key = eval(input("enter key: "))
    message = input("Enter you message here: ")
    for i in message:
        number = ord(i) + key
        coded = chr(number)
        print(coded, end='')


def sphere_area(radius):
    surface_area = 4 * 3.14 * int(radius) ** 2
    return surface_area


def sphere_volume(radius):
    volume = (4/3) * 3.14 * radius ** 3
    return volume


def sum_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sum_n_cubes(n):
    sum_cubes = 0
    for i in range(1, n+1):
        sum_cubes += i ** 3
    return sum_cubes


def encode_better():
    key = (input("enter key: "))
    message = input("Enter you message here: ")
    for i in range(len(message)):
        shift = ord(key[i]) - 97
        coded = chr(ord(message[i]) + shift)
        print(coded, end="")


def main():
    radius = 5
    n = 3

    volume = sphere_volume(radius)
    sa = sphere_area(radius)
    sum = sum_n(n)
    sum_cubes = sum_n_cubes(n)

    print(round(volume, 2))
    print(sa)
    print(sum)
    print(sum_cubes)

    pass


cash_conversion()
encode()
encode_better()
main()
