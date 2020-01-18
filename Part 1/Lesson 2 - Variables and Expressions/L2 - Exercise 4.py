#https://www.py4e.com/html3/02-variables
#Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.
print('Enter Celsius temperature:')
c = input()
c=float(c)
f = (c*(9/5))+32
f=str(f)
print('Farenheit temperature is:' + f)
