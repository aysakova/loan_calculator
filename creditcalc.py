
import math
import sys
import argparse


parser = argparse.ArgumentParser(description="Calculates the desired thing.")

parser.add_argument("--type", choices=["annuity", "diff"], required=True)
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--principal")
parser.add_argument("--interest")

args = parser.parse_args()

if len(sys.argv) < 5:
    print("Incorrect parameters.")
    exit()
elif args.type is None:
    print("Incorrect parameters.")
    exit()

my_type = args.type
if args.principal is not None:
    principal = int(args.principal)
if args.periods is not None:
    periods = int(args.periods)
if args.payment is not None:
    payment = int(args.payment)
if args.interest is not None:
    interest = float(args.interest)

if my_type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
        exit()
    overpayment = 0
    if args.payment is None:
        for m in range(1, periods + 1):
            monthly_pay = math.ceil(principal / periods + interest / 1200 * (principal - (principal * (m - 1)) / periods))
            overpayment += monthly_pay
            print(f"Month {m}: payment is {monthly_pay}")
        print(f"\nOverpayment = {overpayment - principal}")

elif my_type == "annuity":
    if args.payment is None:
        annuity_pay = math.ceil(principal * (interest / 1200 * (1 + interest / 1200) ** periods) / ((1 + interest / 1200) ** periods - 1))
        print(f"Your annuity payment = {annuity_pay}!")
        overpayment = math.ceil(annuity_pay * periods)
        print(f"Overpayment = {overpayment - principal}")
    elif args.principal is None:
        principal = int(payment / ((interest / 1200 * (1 + interest / 1200) ** periods) / ((1 + interest / 1200) ** periods - 1)))
        print(f"Your loan principal = {principal}")
        overpayment = math.ceil(payment * periods)
        print(f"Overpayment = {overpayment - principal}")
    elif args.periods is None:
        value = payment / (payment - interest / 1200 * principal)
        base = 1 + interest / 1200
        n_years = int(math.log(value, base) / 12)
        n_months = math.ceil(math.log(value, base) % 12)
        if n_months == 12:
            n_years += 1
            overpayment = payment * (n_years * 12)
            print(f'It will take {n_years} years to repay this loan!')
        else:
            overpayment = payment * (n_years * 12 + n_months)
            print(f'It will take {n_years} years and {n_months} months to repay this loan!')
        print(f"Overpyayment = {overpayment - principal}")
