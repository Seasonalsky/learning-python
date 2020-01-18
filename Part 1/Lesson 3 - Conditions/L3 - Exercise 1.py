#https://www.py4e.com/html3/03-conditional
#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
print('Enter Hours:')
hours = input()
hours = float(hours)
print('Enter Rate:')
rate = input()
rate = float(rate)
if hours>40:
    rate = rate * 1.5
pay = rate * hours
print ('Pay:' + str(pay))