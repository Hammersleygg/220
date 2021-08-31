"""
Name: <Gavin Hammersley>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the length: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the length: "))
    height = eval(input("Enter the length: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    made = eval(input("Enter the shots made: "))
    total = eval(input("Enter the total shots: "))
    percent = made / total * 100
    print("Percent =", percent)



def coffee():
    cost = 10.50
    shipping = 0.86
    fixed = 1.50
    weight = eval(input("Enter the total pounds: "))
    total = cost * weight + shipping * weight + fixed
    print("Total =", total)


def kilometer_to_miles():
    miles = eval(input("Enter the total miles: "))
    kilometers = 1.61
    traveled = miles * kilometers
    print("Traveled =", traveled)





