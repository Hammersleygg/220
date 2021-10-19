"""
Name: Gavin Hammersley
vigenere.py

Problem: write a program that implement the Vigenere cipher

Certification of authenticity
I certify that this assignment is entirely my own work.
"""
from graphics import *


def main():
    # draw the interface / buttons and inputs
    win = GraphWin("Vigenere", 500, 300)
    win.setCoords(0, 0, 10, 10)

    background = Rectangle(Point(0, 0), Point(500, 500))
    background.setFill("white")
    background.draw(win)

    message_to_code_text = Text(Point(2, 9), "Message to code: ")
    message_to_code_text.setSize(16)
    message_to_code_text.setFace("times roman")
    message_to_code_text.draw(win)

    user_input = Entry(Point(5, 9), 16)
    user_input.draw(win)

    key_word = Text(Point(2, 8), "Enter Keyword: ")
    key_word.setSize(16)
    key_word.setFace("times roman")
    key_word.draw(win)

    user_input2 = Entry(Point(5, 8), 16)
    user_input2.draw(win)

    button_text = Text(Point(5, 5), "Encode")
    button_outline = Rectangle(Point(3, 6), Point(7, 4))
    button_text.draw(win)
    button_outline.draw(win)

    win.getMouse()
    message = user_input.getText()
    key = user_input2.getText()

    # return message,key
    coded = code(message, key)

    # remove the button/ writing the ciphered answer
    button_text.undraw()
    button_outline.undraw()
    button_text = Text(Point(5, 1), coded)
    button_text.draw(win)

    output_label = Text(Point(2, 1), "Ciphered: ")
    output_label.setSize(16)
    output_label.setFace("times roman")
    output_label.draw(win)

    closing_label = Text(Point(5, 5), "Click to close.")
    closing_label.draw(win)
    win.getMouse()


def code(message, key):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    message = message.replace(" ", "")
    k = 0
    output = ""
    # i = message position, if range position of i is > than max length of key and current value of key, k is
    # greater than length of key
    # then reset key position
    for i in range(len(message)):
        if i > len(key) - 1 and k >= len(key) - 1:
            k = 0
        # as long as i in message position is > 0 then accumulate
        else:
            if i > 0:
                k += 1
        # make the key and message numbers
        shift = ord(key[k]) - 97
        coded = ord(message[i]) - 97
        #  shift them into the vigenere and put them into the alphabet
        encipher = (shift + coded) % 26
        alpha = (alphabet[encipher]).upper()
        # append the coded value to the output string
        output += alpha
    return output


main()
