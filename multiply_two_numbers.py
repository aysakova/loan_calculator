# loan_principal = input("Enter the loan principal:\n")
# print(loan_principal)
# result = input('What do you want to calculate?'
#                '\ntype "m" - for number of monthly payments,'
#                '\ntype "p" - for the monthly payment:\n ')
# if result == "m":
#     payment = input("Enter the monthly payment: \n")
#     months = int(loan_principal) / int(payment)
#     if months > 1:
#         print(f'It will take {round(months)} months to repay the loan')
#     else:
#         print(f'It will take {round(months)} month to repay the loan')
#
# else:
#     months = input("Enter the number of months:\n")
#     payment = math.ceil(int(loan_principal) / int(months))
#     last_payment = int(loan_principal) - (int(months) - 1) * int(payment)
#
#     if last_payment == payment:
#         print(f'Your monthly payment = {payment}')
#     else:
#         print(f'Your monthly payment = {payment} and the last payment = {last_payment}')

# output = input('What do you want to calculate?'
#                   '\ntype "n" for number of monthly payments,'
#                   '\ntype "a" for annuity monthly payment amount,'
#                   '\ntype "p" for loan principal:'
#                   '\n')
#
# if output == 'a':
#     print('Enter the loan principal:')
#     p = int(input())
#     print('Enter the number of periods:')
#     n = int(input())
#     print('Enter the loan interest:')
#     i = float(input())
#     a = math.ceil(p * (i / 1200 * (1 + i / 1200) ** n) / ((1 + i / 1200) ** n - 1))
#     print(f"Your monthly payment = {a}!")
#
# elif output == "n":
#     print('Enter the loan principal:')
#     p = int(input())
#     print('Enter the monthly payment:')
#     a = float(input())
#     print('Enter the loan interest:')
#     i = float(input())
#     value = a / (a - i / 1200 * p)
#     base = 1 + i / 1200
#     n_years = int(math.log(value, base) / 12)
#     n_months =math.ceil(math.log(value, base) % 12)
#
#     if n_months == 12 :
#         n_years += 1
#         print(f'It will take {n_years} years to repay this loan!')
#     else:
#         print(f'It will take {n_years} years and {n_months} months to repay this loan!')
#
# elif output == "p":
#     print('Enter the annuity payment:')
#     a = float(input())
#     print('Enter the number of periods:')
#     n = int(input())
#     print('Enter the loan interest:')
#     i = float(input())
#
#     p = int(a / ((i / 1200 * (1 + i / 1200) ** n) / ((1 + i / 1200) ** n - 1)))
#     print(f'Your loan principal = {p}!')
