"""
Name: Gavin Hammersley
interest.py

Problem: Calculate and output the monthly charge

Certification of authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    annual_interest_rate = eval(input("please enter your annual interest rate. ")) / 100
    billing_cycle = eval(input("please enter the number of days in you billing cycle. "))
    net_balance = eval(input("please enter your previous net balance. "))
    payment_amount = eval(input("please enter your payment amount. "))
    day_paid = eval(input("please enter the day your bill was paid. "))
    days_left_in_cycle = billing_cycle - day_paid
    monthly_interest_rate = annual_interest_rate / 12
    part1 = ((net_balance * billing_cycle) - (payment_amount * days_left_in_cycle))
    part2 = part1 / billing_cycle
    monthly_interest_total = part2 * monthly_interest_rate
    print(round(monthly_interest_total, 2))


if __name__ == '__main__':
    main()
    