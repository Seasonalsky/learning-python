#https://www.py4e.com/html3/02-variables
#exercise 2: Write a program to prompt the user for hours and rate per hour to compute gross pay.
print('Enter hours:')
hours = input()
print('Enter rate:')
rate = input()
pay = float(hours) * float(rate)
pay = str(pay)
print('Pay: '+ pay)

