"""
Name: Gavin Hammersley
lab9.py

Problem:

Certification of authenticity
I certify that this assignment is entirely my own work.
"""
from graphics import *


def addTens(nums):
    numbers = []
    for i in nums:
        acc = 10
        acc = i + acc
        numbers.append(acc)
    # print(numbers)


def squareEach(nums):
    numbers = []
    for i in nums:
        new = i ** 2
        numbers.append(new)
    # print(numbers)


def sumList(nums):
    numbers = []
    acc = 0
    for i in nums:
        acc += i
        numbers.append(acc)
    # print(acc)
    return acc


def toNumbers(strList):
    new = []
    for i in range(len(strList)):
        num_list = strList[i]
        new_list_2 = float(num_list)
        new.append(new_list_2)
        # print(new)
    return new


def writeSumOfSquares():
    ask = input("Please enter a file name with at least 2 numbers per line:")

    file_1 = open(ask, 'r')
    file_2 = open(sum_out.txt, 'w')

    for line in file_1:
        line.split()
        sum_line = toNumbers(line)
        sum_line_2 = sumList(sum_line)
        file_2.write(sum_line_2)
        # print(sum_line_2)


def starter():
    weight = eval(input("What is your fighters weight?: "))
    wins = eval(input("How many fights have they won?: "))

    if (weight >= 150) and (weight <= 160) and wins > 5:
        print("This fighter should be a starter.")
    elif (weight > 199) or wins > 20:
        print("This fighter should be a starter.")
    else:
        print("This fighter should not be a starter.")


def leapYear(year):
    num = year
    if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
        print(year, "is a leap year!")
        return True
    elif num % 100 == 0:
        print(year, "is not a leap year.")
        return False


def circleOverlap():
    window = GraphWin("Circle", 500, 500)
    background = Rectangle(Point(0, 0), Point(500, 500))
    background.setFill("red")
    background.draw(window)

    # hard coded circle
    point_a = Point(250, 250)
    circle1 = Circle(point_a, 25)
    circle1.setFill("white")
    circle1.draw(window)

    # user generated circle
    a_point = window.getMouse()

    click_2 = window.getMouse()

    circle2 = Circle(a_point, click_2)
    circle2.draw(window)


def main():
    # add other function calls here
    strList = ['3', '5.7', '2']
    print(strList)
    toNumbers(strList)
    print(strList)
    pass


# main()
# writeSumOfSquares()
# addTens(nums)
# starter()
# leapYear(2010)
# circleOverlap()
