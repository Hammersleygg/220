"""
Name: Gavin Hammersley
greeting.py

Problem: write a program that displays a heart with an arrow moving through it

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

# from graphics import *
from graphics import GraphWin, Rectangle, Point, Text, Image


def main():
    win = GraphWin("Happy Valentines Day!", 500, 500)

    # Draw the background
    background = Rectangle(Point(0, 0), Point(500, 500))
    background.setFill("pink")
    background.draw(win)

    # message
    message = Text(Point(250, 400), "Have a happy Valentines Day!")
    message.setFace("times roman")
    message.setStyle("bold")
    message.setSize(18)
    message.setTextColor("red")
    message.draw(win)

    # Decoration
    line = Image(Point(250, 470), "line2.png")
    line.draw(win)
    line.move(3, 1)
    line2 = Image(Point(250, 330), "line_cut.png")
    line2.draw(win)
    line2.move(-3, 1)

    # Draw heart and arrow / make it move
    heart = Image(Point(250, 250), "heart.png")
    heart.draw(win)

    arrow = Image(Point(-100, 600), "arrow.png")
    arrow.draw(win)

    heart_cut = Image(Point(250, 250), "heart-cutout.png")
    heart_cut.draw(win)

    for _ in range(700):
        arrow.move(3, -3)

    # Closing the card
    message2 = Text(Point(250, 475), "Click to close your card")
    message2.draw(win)
    win.getMouse()
    win.close()


main()
