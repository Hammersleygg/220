"""
Name: Gavin Hammersley
lab6.py

Problem: Work with strings

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first_last_name = input("Please enter your first and last name: ")
    name = first_last_name.split()
    first = name[0]
    last = name[1]
    print(last + "," + first)


def company_name():
    internet_domain = input("Please enter a three part internet domain:")
    company = internet_domain.split(".")
    company_names = company[1]
    print(company_names)


def initials():
    how_many = eval(input("Enter the amount of student that are in the class: "))
    for i in range(how_many):
        first_name = input("Enter the first name of student " + str(i + 1) + ":")
        last_name = input("Enter " + first_name + "'s last name: ")
        initial = first_name[0] + last_name[0]
        print(first_name + "'s initials are " + initial.capitalize())


def names():
    all_name = input("Enter people's names, separated by commas: ")
    separate = all_name.split(",")
    print("The initials are ", end=" ")
    for i in range(len(separate)):
        names = separate[i].split()
        first = names[0]
        last = names[1]
        initial = first[0] + last[0]
        print(initial.capitalize())


def thirds():
    number_sentences = input("Enter the number of sentences you have: ")
    sentences = input("Enter your sentences: ")
    length = len(sentences)
    for i in range(len(number_sentences)):
        for x in range(2, length, 3):
            print(sentences[x], end="")


def word_average():
    number_of_sentence = eval(input("Enter the number of sentences: "))
    acc = 0
    for i in range(number_of_sentence):
        sentence = input("Enter your sentence here: ")
        split = sentence.split(" ")
        for x in range(len(split)):
            word = split[x]
            acc += len(word)
        avg = acc / len(split)

        print(avg)


def pig_latin():
    sentence = input("Enter your sentence here: ")
    words = sentence.split()
    single = words[0:-1]
    for i in range(len(single)):
        pig1 = single[0]
        pig2 = single[1:3]
    print(pig2 + "ay" + pig1)


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
