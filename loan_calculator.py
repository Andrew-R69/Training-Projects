import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=float, default=0, required=False, help='Loan principal amount')
parser.add_argument('--payment', type=float, default= 0, required=False, help='Monthly payment amount')
parser.add_argument('--periods', type=int, default = 0, required=False, help='Number of months to repay the loan')
parser.add_argument('--interest', type=float, required=False, help='Annual interest rate in percent')
parser.add_argument('--type', type=str, required=False, help='Type of payment: annuity or differentiated')
args = parser.parse_args()

def error_print():
    print("Incorrect parameters")
    exit(1)

if not args.interest or not args.type:
    error_print()

if args.type == 'diff' and args.payment:
    error_print()

if args.principal < 0 or args.payment < 0 or args.periods < 0 or args.interest < 0:
    error_print()

counter = 0

for arg in [args.principal, args.payment, args.periods]:
    if arg:
        counter += 1
if counter < 2 or counter >= 3:
    error_print()

def calculate_principal(interest, payment, periods):
    monthly_interest = interest / (100 * 12)
    principal = payment / ((monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1))
    return print(f"Your loan principal = {math.floor(principal)}! \nOverpayment = {math.ceil(payment * periods - principal)}")

def calculate_payment(interest, principal, periods):
    monthly_interest = interest / (100 * 12)
    total_payment = 0
    payment = math.ceil(principal * (monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1))
    total_payment = payment * (periods)
    return print(f"Your annuity payment = {payment}! \nOverpayment = {math.ceil(total_payment - principal)}")

def calculate_periods(interest, principal, payment):
    monthly_interest = interest / 100 / 12
    periods = math.ceil(math.log(float(payment) / (float(payment) - monthly_interest * float(principal)), 1 + monthly_interest))
    total_payment = payment * periods
    if periods < 12:
        return print(f"It will take {periods} months to repay the loan. \nOverpayment = {math.ceil(total_payment - principal)}")
    else:
        years = periods // 12
        months = periods % 12
        if months == 0:
            return print(f"It will take {years} years to repay the loan. \nOverpayment = {math.ceil(total_payment - principal)}")
        else:
            return print(f"It will take {years} years and {months} months to repay the loan. \nOverpayment = {math.ceil(total_payment - principal)}")
            
def calculate_diff_payment(interest, principal, periods):
    monthly_interest = interest / (100 * 12)
    total_payment = 0
    for month in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods + monthly_interest * (principal - (principal * (month - 1) / periods)))
        print(f"Month {month}: payment is {diff_payment}")
        total_payment += diff_payment
    print ("Overpayment = ", math.ceil(total_payment - principal))
if args.type == 'annuity' or args.type == 'diff':
    if args.type == 'diff':
        calculate_diff_payment(args.interest, args.principal, args.periods)
    elif not args.principal:
        calculate_principal(args.interest, args.payment, args.periods)
    elif not args.payment:
        calculate_payment(args.interest, args.principal, args.periods)
    else:
        calculate_periods(args.interest, args.principal, args.payment)
else:
    error_print() 