"""
Name: Gavin Hammersley
lab8.py

Problem:

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    lines = 0
    words = 0

    for line in in_file:
        word_list = line.split()
        lines = lines + 1
        words = words + len(word_list)
        out_file.write(str(words))
        for word in word_list:
            # print(word)
            out_file.write("\n" + word)


def hourly_wage(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    for words in in_file:
        in_file = words.split(" ")
        first_last = in_file[0:2]
        out_file.write("\n" + str(first_last))
        print(first_last)

        raise_wage1 = in_file[4] * int(1.65)
        new_wage = in_file[3] + raise_wage1
        out_file.write("\n" + new_wage)

        print(new_wage)


def calc_check_sum(isbn):
    split = [int(i) for i in isbn]
    print(split)
    x = 1
    total = 0
    for i in split:
        new = split[i] * x
        x += 1
        total += new
        print(total)


def main():
    number_words("Walrus.txt", "Walrus_output.txt")
    hourly_wage("hourly_wages.txt", "hourly_wages_out.txt")
    calc_check_sum("0072946520")
    # add other function calls here
    # pass


main()
