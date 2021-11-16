"""
Name: Gavin Hammersley
lab11.py

Problem: write a program to support the children's spelling game hangman

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

from random import choice


def read_word(file):
    words = []
    for i in file:
        words.append(i.strip("\n"))
    secret_word = choice(words)
    return secret_word


def guessed_letter(guess, already_letter, wrong_guess, turns_left, secret_word):

    # deals with the guesses if they are wrong, right, too many letters
    turns_left = len(secret_word)
    if guess in already_letter:
        print("That letter has been guessed, try again!")
        return False

    if len(guess) != 1:
        print("You are only allowed to guess one at a time!")
        return False

    if guess in secret_word:
        already_letter.append(guess)
    else:
        already_letter.append(guess)
        wrong_guess.append(guess)
        turns_left += 1


def guessed_word(letter, secret_word, game):
    for i in range(len(secret_word)):
        if secret_word[i] in letter:
            game[i] = secret_word[i]


def game_won(game, secret_word):
    if game == secret_word:
        return True


def main():
    # sets list to hold turns and guessed letters
    turns_left = [0]
    letter_guess = []
    wrong_letters = []

    # open the file for the words of the game
    file = open("wordlist.txt", 'r')

    # Choose the word and start game
    secret_word = read_word(file)
    game = []
    for i in range(len(secret_word)):
        game.append("_")

    # Play the game
    while turns_left[0] < 7:
        print(game)
        print("Wrong letters: {}".format(wrong_letters), '\n')
        print("Turns left {}".format(turns_left))

        guesses = input("Enter your guess here: ")
        print("\n")

        guessed_letter(guesses, letter_guess, wrong_letters, turns_left, secret_word)
        guessed_word(letter_guess, secret_word, game)
        if game_won(game, secret_word) is True:
            break
    if game_won(game, secret_word) is True:
        print("YAY, you won the game!")
    else:
        print("Aw no you lost, try again!")


main()
