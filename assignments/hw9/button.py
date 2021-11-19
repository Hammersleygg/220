"""
Name: Gavin Hammersley
threeDoorGame.py

Problem: write a program and class to draw three doors and make the user
guess what door is the correct door

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import Text


class Button:
    """initializes the doors"""
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        """
        gets a label to be used for doors
        """
        return self.text.getText()

    def draw(self, win):
        """
        used to help draw the doors
        """
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """
        used to draw doors
        """
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """
        gets range based off of where you click on the doors
        """
        x_doors = range(int(self.shape.getP1().getX()), int(self.shape.getP2().getX()))
        y_doors = range(int(self.shape.getP1().getY()), int(self.shape.getP2().getY()))
        return (round(point.getX()) in x_doors) and (round(point.getY()) in y_doors)

    def color_button(self, color):
        """
        fills the color of doors
        """
        self.shape.setFill(color)

    def set_label(self, label):
        """
        sets the label to be used for doors
        """
        self.text.setText(label)
