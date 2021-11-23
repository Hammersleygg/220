"""
Name: Gavin Hammersley
lab12.py

Problem: use while in order to loop rather than for

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

from random import randint
from algorithms import read_data, is_in_linear


def find_and_remove_first(list, value):
    list.insert(list.index(value), "Gavin")
    list.remove(value)


def good_input():
    good_value = int(input("Enter a number that is between 1- 10"))
    while not 1 <= good_value <= 10:
        good_value = input("Value was not in between 1 and 10. Please enter another value.")
        return good_value


def num_digits():
    number = 1
    while number >= 1:
        number = eval(input("Enter a positive number greater than 0: "))
        digits = 0
        if number >= 1:
            while number != 0:
                number //= 10
                digits += 1
            print(digits)


def hi_lo_game():
    random_number = randint(1, 100)
    guess_count = 0
    guess = 0
    while guess_count < 7 and guess != random_number:
        guess = int(input("Guess a random number 1-100: "))
        if guess < random_number:
            print("Too low, Try again.")
            guess_count += 1
        if guess > random_number:
            print("Too high, Try again.")
            guess_count += 1
        if guess == random_number:
            print("You figured it out in {} guesses!".format(guess_count))
        if guess_count == 7:
            print("You've ran out of guesses. The correct number was {}".format(random_number))


def main():
    # print(find_and_remove_first([1, 2, 3, 5], 2))
    # print(good_input())
    # num_digits()
    hi_lo_game()


main()

"""
algorithms.py work

def read_data(filename):
    val_list = []
    file = open(filename, "r")
    line = file.readline()
    while line != '':
        split_line = line.split()
        count = 0
        while count < len(split_line):
            val_list.append(eval(split_line[count]))
            count += 1
        line = file.readline()
    return val_list


def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if search_val == values[count]:
            return True
        count += 1
        # print(count)
    return False
"""
