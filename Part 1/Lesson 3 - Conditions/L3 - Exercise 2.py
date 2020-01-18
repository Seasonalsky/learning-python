#https://www.py4e.com/html3/03-conditional
#Exercise 2: Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
try:
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
except:
    print('Error, please enter numeric input')