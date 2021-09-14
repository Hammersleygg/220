"""
Name: Gavin Hammersley
lab3.py

Problem: develop simple python programs that use for loops

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def average():
    grades = 0
    number_of_grades = eval(input("Enter the number of grades you have: "))
    for i in range(0, number_of_grades):
        total = eval(input("Enter you grade on HW" + str(i + 1) + ": "))
        grades += total
        avg = grades / number_of_grades
    print("This is your average of Homeworks:", round(avg, 2))


def tip_jar():
    money = 0
    for i in range(0, 5):
        ask = eval(input("Enter the amount you will be tipping,person:" + str(i + 1)))
        money += ask
    print("this is the total amount of tips: $", round(money, 2))


def newton():
    x = eval(input("Enter your number here: "))
    improve = eval(input("Enter the number of times you want to improve here:"))
    approx = x / 2
    for i in range(0, improve):
        approx = ((approx + (x / approx)) / 2)
    print("This is your improved number:", round(approx, 2))


def sequence():
    number_of_terms = eval((input("Enter the number of terms in your series: ")))
    x = 1
    for i in range(number_of_terms):
        x = x + i % 2 * 2
        print(x)


def pi():
    number_of_terms = eval((input("Enter the number of terms in your series: ")))
    x = 1
    total = 1
    for i in range(number_of_terms):
        x = x + i % 2 * 2
        y = (i + 1) % 2 + (i + 1)
        total = total * (y / x)
        print(total * 2)
