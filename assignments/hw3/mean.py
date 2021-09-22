"""
Name: Gavin Hammersley
convert.py

Problem: create a program that asks for input, does arithmetic and provides output

Certification of authenticity
I certify that this assignment is entirely my own work.
"""
import math

# this program will ask for input, do arithmetic and provide output
# inputs are number of values to be entered
# outputs are the actual values
# steps:
# 1. ask for the number of values
# 2. ask for the actual values
# 3. put them into the equation to get the RMS, Harmonic Mean and Geometric mean


def main():
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1

    input_numbers = eval(input("Enter the values to be entered: "))
    for i in range(input_numbers):
        input_values = eval(input("Enter the value " + str(i + 1) + ": "))
        rms_average += input_values ** 2
        harmonic_mean += 1 / input_values
        geometric_mean *= input_values

    rms_average /= input_numbers
    harmonic_mean = input_numbers / harmonic_mean
    geometric_mean = geometric_mean ** (1 / input_numbers)

    print(round(math.sqrt(rms_average), 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
