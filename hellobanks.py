import math
import sys
args = sys.argv
type = ''
interest = ''
principal = ''
periods = ''
payment = ''


def months_to_year(month):
    years = month // 12
    mines = month % 12
    if mines == 1 and years == 0:
        print("It will take 1 month to repay the loan")
    elif years == 0 and mines >= 1:
        print(f'It will take {mines}  months to repay the loan')
    elif years > 0 and mines == 0:
        print(f'"It will take {years} years to repay the loan')
    else:
        print(f'"It will take {years} years and {mines} months to repay the loan')


for o in range(1, len(args)):
    if "type" in args[o]:
        type = args[o]
    if "principal" in args[o]:
        principal = args[o]
    if 'periods' in args[o]:
        periods = args[o]
    if "payment" in args[o]:
        payment = args[o]
    if "interest" in args[o]:
        interest = args[o]

if (type != "--type=annuity" and type != "--type=diff") or type == '' or interest == '' or len(args) < 5:
    print("Incorrect parameters.")

elif type == "--type=diff":
    if payment != "":
        print("Incorrect parameters.")
    else:
        real_principal = int(principal[12:])
        real_periods = int(periods[10:])
        real_interest = float(interest[11:])
        if real_principal < 0 or real_periods <0 or real_interest <0:
            print("Incorrect parameters.")
        else:
            i = real_interest / (12 * 100)
            extra = 0
            for month in range(1, real_periods + 1):
                payment1 = math.ceil((real_principal / real_periods) + i * (real_principal - ((real_principal * (month - 1 )) / real_periods)))
                print(f'Month {month}: payment is {payment1}')
                extra += payment1

            overpayment = extra - real_principal
            print("Overpayment = ", overpayment)
elif type == "--type=annuity" and principal == '':
    real_periods = int(periods[10:])
    real_payment = int(payment[10:])
    real_interest = float(interest[11:])
    if real_periods <0 or real_payment < 0 or real_interest < 0:
        print("Incorrect parameters.")
    else:
        i = real_interest / (12 * 100)
        loan = useful = (i * ((1 + i) ** real_periods)) / (((1 + i) ** real_periods) - 1)
        loan2 = (real_payment / useful)
        extra = real_payment * real_periods
        overpayment = extra - loan2
        print(f'Your loan principal = {math.floor(loan2)}!')
        print(f'Overpayment = {math.ceil(overpayment)}')
elif type == "--type=annuity" and periods == '':
    real_principal = int(principal[12:])
    real_payment = int(payment[10:])
    real_interest = float(interest[11:])
    if real_principal <0 or real_payment < 0 or real_interest < 0:
        print("Incorrect parameters.")
    else:
        i = real_interest / (12 * 100)
        n = math.log(real_payment / (real_payment - i * real_principal), 1 + i)
        months_to_year(math.ceil(n))
        extra = math.ceil(n) * real_payment
        overpayment = extra - real_principal
        print(f'Overpayment = {overpayment}')
elif type == "--type=annuity" and payment == '':
    real_principal = int(principal[12:])
    real_periods = int(periods[10:])
    real_interest = int(interest[11:])
    if real_principal < 0 or real_periods < 0 or real_interest < 0:
        print("Incorrect parameters.")
    else:
        i = real_interest / (12 * 100)
        real_payment = real_principal * (i * ((1 + i) ** real_periods)) / (((1 + i) ** real_periods) - 1)
        print(f'Your monthly payment = {math.ceil(real_payment)}')
        extra = math.ceil(real_payment) * real_periods
        overpayment = extra - real_principal
        print(f'Overpayment = {overpayment}')









#print(type, principal ,periods, payment, interest)

#real_principal = int(principal[12:])
#real_periods = int(periods[10:])
#real_payment = int(payment[10:])
#real_interest = int(interest[11:])
#print(real_periods)