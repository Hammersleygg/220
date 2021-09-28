"""
Name: Gavin Hammersley
lab5.py

Problem: use graphics to write code

Certification of authenticity
I certify that this assignment is entirely my own work.
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    point_a = Point(250, 250)
    point_b = point_a
    point_c = point_a
    circle_a = Circle(point_a, 275)
    circle_b = Circle(point_b, 137.5)
    circle_c = Circle(point_c, 68.75)

    circle_a.setFill("red")
    circle_b.setFill("blue")
    circle_c.setFill("white")

    circle_a.draw(win)
    circle_b.draw(win)
    circle_c.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    message = Text(Point(250, 450), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("green")
    triangle.setOutline("blue")
    triangle.draw(win)

    dx1 = p2.getX() - p1.getX()
    dx2 = p2.getX() - p3.getX()
    dx3 = p3.getX() - p1.getX()
    dy1 = p2.getY() - p1.getY()
    dy2 = p2.getY() - p3.getY()
    dy3 = p3.getY() - p1.getY()

    a = math.sqrt(dx1 ** 2 + dy1 ** 2)
    b = math.sqrt(dx2 ** 2 + dy2 ** 2)
    c = math.sqrt(dx3 ** 2 + dy3 ** 2)

    s = (a + b + c) / 2
    inside = s * (s - a) * (s - b) * (s - c)
    area_t = math.sqrt(round(inside, 2))

    text1 = Text(Point(60, 100), area_t)
    text1.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_input = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_input.draw(win)
    green_input = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_input.draw(win)
    blue_input = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_input.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_input.getText())
        green = int(green_input.getText())
        blue = int(blue_input.getText())

        color = color_rgb(red, green, blue)
        shape.setFill(color)

    msg2 = "click to close window"
    inst2 = Text(Point(win_width / 2, win_height - 50), msg2)
    inst2.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("please enter your string: ")

    # first character in string
    first_character = user_string[0]
    print(first_character)
    # last character of string
    last_character = user_string[-1]
    print(last_character)
    # characters inclusively in positions 2 – 5 of the string
    positions_2_5 = user_string[1:6]
    print(positions_2_5)
    # concatenation of the first and last character of the string
    first = user_string[0]
    last = user_string[-1]
    concatenation = first + last
    print(concatenation)
    # The first three characters in the string repeated 10 times
    for i in range(10):
        first_3 = user_string[0:3]
        print(first_3)

    # Each character in the string printed one character per line
    for i in range(user_string):
        print(user_string[0:-1])

    # The number of characters in the string
    print(len(user_string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    # make x the string "hithere"
    first = values[1]
    last = values[3]
    hi_there = first + last
    print(hi_there)
    # make x the sum of 5 and 2.5
    sum_x = values[0]
    sum_y = values[2]
    print(sum_x + sum_y)
    # make x the string "hihihihihi"
    for i in range(5):
        print(values[1])
    # make x the list [2.5, "there", pt]
    x = [2.5, "there", pt]
    print(x)
    # make x the list [2.5,5,7.2]
    x = [2.5, 5, 7.2]
    print(x)
    # make x the sum of 5 + 2.5 + 7.2
    sum2 = values[0]
    sum3 = values[2]
    sum4 = eval(values[5])
    print(sum2 + sum3 + sum4)
    # make x the number of items in value
    print(len(values))


def another_series():
    number_of_terms = eval((input("Enter the number of terms to sum: ")))
    total = 0
    for i in range(number_of_terms):
        x = i % 3
        even = 2 * x + 2
        total += even
        print(even)
    print("sum: ", total)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
