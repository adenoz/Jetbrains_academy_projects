# THIS REMAINS A WORK IN PROGRESS!
# Notes. I just completed the initial draft calculations and variable assignments.
# They remain raw. So I next need to consider rounding up or to confirm float v int etc.
# I also haven't fully confirmed all calculations are complete or correct. Here.

import math

# DATA CAPTURE

print('What do you want to calculate?\ntype "n" for number of monthly payments,'
      '\ntype "a" for annuity monthly payment amount,\ntype "p" for loan principal:')
want = input()

if want != 'p':
    print("Enter the loan principal:")
    principal = int(input())

if want != 'a':
    print("Enter the monthly payment:")
    m_payment = int(input())

if want != 'n':
    print("Enter the number of periods:")
    n_periods = int(input())

print("Enter the loan interest:")
interest = float(input())

# DATA SHAPING AND WRANGLING

loan_interest = interest / 12 * 100

principal_calc = m_payment / (loan_interest * (1 + loan_interest)**n_periods / (1 + loan_interest)**n_periods - 1)

m_payment_calc = principal * (loan_interest * (1 + loan_interest)**n_periods / (1 + loan_interest)**n_periods - 1)

n_periods_calc = math.log(1 + loan_interest) * (m_payment / m_payment - loan_interest * principal)

n_rounded = round(n_periods_calc)  # Is using the round() function what I was thinking here?

if n_rounded <= 12:
    n_month_only == n_rounded
elif n_rounded > 12:
    n_years = n_rounded // 12
    n_months = n_rounded % 12

time = principal / m_payment

# THE OUTPUTS

if want == 'p':
    print(f"Your loan principal = {principal_calc}!")

if want == 'a':
    print(f"Your monthly payment = {m_payment_calc}!")

if want == 'n':
    if n_rounded < 13:
        print(f"It will take {n_month_only} months to repay this loan!")
    elif n_rounded > 12:
        print(f"It will take {n_years} years and {n_months} months to repay this loan!")



###---------------------------
#
# if time <= 1:
#     print(f"It will take {math.ceil(time)} month to repay the loan")
# elif time > 1:
#     print(f"It will take {math.ceil(time)} months to repay the loan")
#
# if want == 'p':
#     print("Enter the number of months:")
#     n_months = int(input())
#     payment = principal / n_months
#     last = principal - (n_months - 1) * math.ceil(payment)
#     print(f"Your monthly payment = {math.ceil(payment)} and the last payment = {math.ceil(last)}.")
