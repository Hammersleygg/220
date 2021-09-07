"""
Name: Gavin Hammersley
lab2.py

Problem: use the python math library to write functions
"""
import math


def sum_of_threes():
    sum_of_multiples = 0
    upper_bound = eval(input("enter your upper bound here."))
    for i in range(3, upper_bound, 3):
        sum_of_multiples += i
        print(sum_of_multiples)


def muliplication_table():
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    for row in range(1, 11):
        print(row, ":")
        for column in range(1, 11):
            print(row * column, end=" ")


def triangle_area():
    a = eval(input("enter a value here. "))
    b = eval(input("enter b value here. "))
    c = eval(input("enter c value here. "))
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(x)
    print(area)


def sumSquares():
    sum_squares = 0
    lower_range = eval(input("enter lower range here. "))
    upper_range = eval(input("enter upper range here. "))
    for i in range(lower_range, upper_range + 1):
        sum_squares += (i ** 2)
        print(sum_squares)


def power():
    base = eval(input("enter base value here. "))
    exponent = eval(input("enter exponent here. "))
    total = base ** exponent
    print(total)
