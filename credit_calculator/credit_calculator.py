import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--annuity", type=float)
parser.add_argument("--type", type=str)
args = parser.parse_args()


def n(principal, payment, interest):
    percent = float(interest / (12 * 100))
    months = math.ceil(math.log(payment / (payment - percent * principal), 1 + percent))
    years = months // 12
    months_remaining = months % 12

    if years > 0 and months_remaining > 0:
        print(f"It will take {years} years and {months_remaining} months to repay this loan!")
    elif years > 0:
        print(f"It will take {years} years to repay this loan!")
    elif months_remaining > 0:
        print(f"It will take {months_remaining} months to repay this loan!")


def a(principal, periods, interest):
    percent = float(interest / (12 * 100))
    annuity = math.ceil(
        principal * ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your monthly payment = {annuity}!")


def p(payment, periods, interest):
    percent = float(interest / (12 * 100))
    principal = round(
        payment / ((percent * ((1 + percent) ** periods)) / (((1 + percent) ** periods) - 1)))
    print(f"Your loan principal = {principal}!")


def d(principal, periods, interest):
    percent = float(interest / (12 * 100))
    remaining_principal = principal
    payments = []
    for month in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods) + percent * (
                remaining_principal - (principal * (month - 1)) / periods)
        payments.append(diff_payment)
        remaining_principal -= principal / periods
        print(f"Month {month}: payment is {diff_payment}")

    total_payment = sum(payments)
    overpayment = total_payment - principal
    print(f"\nTotal payment: {total_payment}")
    print(f"Overpayment: {overpayment}")


if args.type == "annuity":
    if args.payment is not None and args.principal is not None and args.interest is not None:
        if args.principal > 0 and args.payment > 0 and args.interest > 0:
            n(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters!")
    elif args.principal is not None and args.periods is not None and args.interest is not None:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            a(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters!")
    elif args.payment is not None and args.periods is not None and args.interest is not None:
        if args.payment > 0 and args.periods > 0 and args.interest > 0:
            p(args.payment, args.periods, args.interest)
        else:
            print("Incorrect parameters!")
    else:
        print("Incorrect parameters!")
elif args.type == "diff":
    if args.principal is not None and args.periods is not None and args.interest is not None:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            d(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters!")
    else:
        print("Incorrect parameters!")
else:
    print("Incorrect parameters!")
