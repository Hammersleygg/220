"""
Name: Gavin Hammersley
lab4.py

Problem: use the author-supplied graphics package, practice accumulating sequence

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(25, 25))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        objectCopy = shape.clone()
        shape = objectCopy
        shape.draw(win)
        shape.move(dx, dy)

        # when clicked, created a new rectangle drawn on the screen
        objectCopy = shape.clone()
        shape = objectCopy
        shape.draw(win)

    inst_pt = Point(width / 2, height - 100)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Draw a rectangle", 700, 500)
    message = Text(Point(350, 10), "Click on two opposite points")
    message.draw(win)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)

    rec = Rectangle(point1, point2)
    rec.draw(win)

    rec.setFill("Blue")
    rec.setOutline("Black")

    dx = abs(point1.getX() - point2.getX())
    dy = abs(point1.getY() - point2.getY())

    length = dx
    width = dy

    area = length * width
    perimeter = 2 * (length + width)

    message_1 = Text(Point(50, 100), area)
    message_2 = Text(Point(50, 200), perimeter)
    message_1.setTextColor("Red")
    message_2.setTextColor("Red")

    message_1.draw(win)
    message_2.draw(win)

    message = Text(Point(350, 450), "Click again to close.")
    message.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 700, 500)
    message = Text(Point(350, 10), "Click on two points to create a circle")
    message.draw(win)

    point1 = win.getMouse()
    point1.draw(win)
    point2 = win.getMouse()
    point2.draw(win)

    dx = abs(point1.getX() - point2.getX())
    radius = dx

    d = point2.getX() - point1.getX()
    y = point2.getY() - point1.getY()

    circle_1 = Circle(point1, radius)
    circle_1.draw(win)
    circle_1.setFill("Blue")

    euclidean_distance = round(math.sqrt(d ** 2 + y ** 2), 2)
    message_1 = Text(Point(60, 100), euclidean_distance)
    message_1.setTextColor("Red")
    message_1.draw(win)

    message = Text(Point(350, 450), "Click again to close.")
    message.draw(win)

    win.getMouse()
    win.close()


def pi2():
    number_of_terms = eval((input("Enter the number of terms to sum: ")))
    switch = -1
    pi = 0
    for i in range(number_of_terms):
        x = 2 * i + 1
        y = 4 / x
        switch = switch * -1
        pi = pi + y * switch
        print(pi)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
