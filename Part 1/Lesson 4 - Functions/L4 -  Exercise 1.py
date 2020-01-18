#https://www.py4e.com/html3/04-functions
#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate):
    if hours>40:
        rate = rate * 1.5
    pay = rate * hours
    print ('Pay:' + str(pay))

computepay(45, 4)