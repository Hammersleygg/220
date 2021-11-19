"""
Name: Gavin Hammersley
threeDoorGame.py

Problem: write a program and class to draw three doors and make the user
guess what door is the correct door

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Rectangle, Text, Point
from button import Button


# used to store the doors and see what one is clicked
def your_pick(picked, door_one, door_two, door_three):
    door = ""
    if door_one.is_clicked(picked) is True:
        door = door_one

    elif door_two.is_clicked(picked) is True:
        door = door_two

    elif door_three.is_clicked(picked) is True:
        door = door_three
    return door


def main():
    # draw window, the doors and set up the game.
    win = GraphWin("Three Door Game", 400, 400)
    background = Rectangle(Point(0, 0), Point(500, 500))
    background.setFill("white")
    background.draw(win)

    start_word = Text(Point(200, 50), "I Have A Secret Door")
    start_word.setSize(16)
    start_word.setFace("times roman")
    start_word.draw(win)

    button_one = Rectangle(Point(125, 100), Point(25, 350))
    button_two = Rectangle(Point(250, 100), Point(150, 350))
    button_three = Rectangle(Point(375, 100), Point(275, 350))

    # create the buttons/doors
    door_one = Button(button_one, "Door 1")
    door_two = Button(button_two, "Door 2")
    door_three = Button(button_three, "Door 3")

    door_one.draw(win)
    door_two.draw(win)
    door_three.draw(win)

    # determine what door is a winner
    start = 1
    end = 3
    winning_door = int(randint(start, end))

    # door_one = eval(str(1))
    # door_two = eval(str(2))
    # door_three = eval(str(3))

    winner = ""
    if winning_door == 1:
        winner = door_one

    elif winning_door == 2:
        winner = door_two

    elif winning_door == 3:
        winner = door_three

    # messages based on your luck when clicking
    winner_message = Text(Point(200, 50), "You Win!")
    loser_message = Text(Point(200, 50), "Sorry you lost.")
    correct_door = Text(Point(200, 370), "Door {} was my secrete door.".format(winner))
    closing_message = Text(Point(200, 380), "Click again to close the game.")

    # playing the game and what happens if your guess is right or wrong
    picked = win.getMouse()

    if your_pick(picked, door_one, door_two, door_three) == winner:
        your_pick(picked, door_one, door_two, door_three).color_button("green")
        start_word.undraw()
        winner_message.draw(win)
        closing_message.draw(win)
    else:
        your_pick(picked, door_one, door_two, door_three).color_button("red")
        start_word.undraw()
        loser_message.draw(win)
        correct_door.draw(win)
        closing_message.draw(win)

    # use to close game
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
