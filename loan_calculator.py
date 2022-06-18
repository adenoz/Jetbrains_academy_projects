import math

print("Enter the loan principal:")
principle = int(input())
print('What do you want to calculate?\n type "m" for number of monthly payments,\n type "p" for the monthly payment:')
want = input()
if want == 'm':
    print("Enter the monthly payment")
    m_payment = int(input())
    time = principle / m_payment
    if time <= 1:
        print(f"It will take {math.ceil(time)} month to repay the loan")
    elif time > 1:
        print(f"It will take {math.ceil(time)} months to repay the loan")

if want == 'p':
    print("Enter the number of months:")
    n_months = int(input())
    payment = principle / n_months
    last = principle - (n_months - 1) * math.ceil(payment)
    print(f"Your monthly payment = {math.ceil(payment)} and the last payment = {math.ceil(last)}.")