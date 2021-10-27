"""
Name: Gavin Hammersley
weighted_average.py

Problem:

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    file1 = open(in_file_name, 'r')
    file2 = open(out_file_name, 'w')

    class_average = 0
    total_students = 0

    for i in file1:
        list1 = i.split(":")
        name = list1[0]
        numbers = list1[1].split()

        weight_total = 0
        for x in numbers[::2]:
            weight_total += int(x)

        average = 0
        if weight_total == 100:
            for y in range(len(numbers[::2])):
                average += int(numbers[y]) * int(numbers[y + 1])
            average = average / 100
            print(name + "'s average: " + str(average), file=file2)
            class_average += average
            total_students += 1
        elif weight_total > 100:
            print(name + "'s average: ERROR: The weights are more than 100.")
        elif weight_total < 100:
            print(name + "'s average: ERROR: The weights are less than 100.")
    class_average = class_average / total_students
    print("Class average: " + str(class_average), file=file2)


weighted_average("grades.txt", "avg.txt")
