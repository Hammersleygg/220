"""
Name: Gavin Hammersley
lab13.py

Problem: preform binary search on data and solve real world problems

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def star_find(filename):
    file = open(filename, 'r')
    line = file.readline()

    initial_list = []
    number = line.split(' ')
    initial_list.append(number)

    strength_signal = []
    number_pulses = 0
    fifth_signal_maybe = 0
    times_looked = 0

    for signal in number:
        fifth_signal_maybe += 1
        if 4000 <= eval(signal) <= 5000:
            strength_signal.append(signal)
            number_pulses += 1
        if number_pulses == 5:
            times_looked = fifth_signal_maybe
            break

    print("This is the number of strong pulses found: ", number_pulses)
    print("This is the strength of each strong pulse: ", strength_signal)
    print("This is the how many signals we had to go through to find a fifth signal: ", times_looked)


# how many pulses (0-5), strength of each signal, if a 5th is found print how many you had to search through before
# you found it.


def main():
    star_find("signals.txt")
    # add other function calls here
    pass


main()
