
# This is the Loan calculator project in the python track in Jetbrains / Hyperskill
# Currently it is at stage 3 of 4.

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
    m_payment = float(input())

if want != 'n':
    print("Enter the number of periods:")
    n_periods = int(input())

print("Enter the loan interest:")
interest = float(input())

# DATA SHAPING AND WRANGLING

loan_interest = interest / (12 * 100)

# We only need to use the input figures for all calculations below.
# Do not use any calculated figures.

if want == 'p':  # this is the loan principal
    bottom_top = loan_interest * (1 + loan_interest)**n_periods
    bottom_bottom = (1 + loan_interest)**n_periods - 1
    principal_calc = m_payment / (bottom_top / bottom_bottom)

if want == 'a':  # this is the monthly annuity payment
    top = loan_interest * (1 + loan_interest)**n_periods
    bottom = (1 + loan_interest)**n_periods - 1
    m_payment_calc = principal * (top / bottom)

if want == 'n':  # this is the number of monthly payments
    main = (m_payment / (m_payment - (loan_interest * principal)))
    to_log = 1 + loan_interest
    n = math.log(main, to_log)
    n_rounded = math.ceil(n)
    if n_rounded <= 12:
        n_month_only = n_rounded
    elif n_rounded > 12:
        n_years = n_rounded // 12
        n_months = n_rounded % 12

# THE OUTPUTS

if want == 'p':
    print(f"Your loan principal = {round(principal_calc)}!")

if want == 'a':
    print(f"Your monthly payment = {math.ceil(m_payment_calc)}!")

if want == 'n':
    if n_rounded < 13:
        print(f"It will take {n_month_only} months to repay this loan!")
    elif n_rounded > 12:
        print(f"It will take {n_years} years and {n_months} months to repay this loan!")
