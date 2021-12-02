"""
Name: Gavin Hammersley
sales_force.py

Problem: write a class that uses the sales person class

Certification of authenticity
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:

    """ creates the sales force class"""
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as file:
            for i in file:
                split_lines = i.split(",")
                sale_amount = split_lines[2].split()
                self.sales_people.append(SalesPerson(int(split_lines[0]), split_lines[1].lstrip()))
                for sale in sale_amount:
                    self.sales_people[-1].enter_sale(float(sale))

    def quota_report(self, quota):
        element_list = []
        for person in self.sales_people:
            who_are_they = [int(person.get_id()), person.get_name(),
                            float(person.total_sales()), person.met_quota(quota)]
            element_list.append(who_are_they)
        return element_list

    def top_seller(self):
        top_person = []
        current_best = 0
        for person in self.sales_people:
            if person.total_sales() > current_best:
                current_best = person.total_sales()

        for person in self.sales_people:
            if person.total_sales() == current_best:
                top_person.append(person)
        return top_person

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
