"""
Name: Gavin Hammersley
traffic.py

Problem: write a program that will help analyze traffic patterns

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    final_total = 0
    for i in range(roads_surveyed):
        total = 0
        days = eval(input("How many days was road " + str(i + 1) + " surveyed?"))
        for x_days in range(days):
            cars = eval(input("How many cars traveled on day " + str(x_days + 1) + " ?"))
            total += cars
            final_total += cars
            average_vehicles = total / days
            average_number = final_total / roads_surveyed
        print("Road" + str(i + 1) + " average vehicles per day: " + str(round(average_vehicles, 2)))
    # print(total)
    # print(days)
    print("Total number of vehicles traveled on all roads: " + str(round(final_total, 2)))
    print("Average number of vehicles per road: " + str(round(average_number, 2)))


if __name__ == '__main__':
    main()
