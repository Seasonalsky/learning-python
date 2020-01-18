#https://www.py4e.com/html3/04-functions
#Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a string.
def computegrade(score):
    if score >= (0.9) and score < 1:
        print('A')
    elif score >= (0.8) and score < 1:
        print('B')
    elif score >= (0.7) and score < 1:
        print('C')
    elif score >= (0.6) and score < 1:
        print('D')
    elif score < (0.6) and score >= 0:
        print('F')
    else:
        print('Score is out of range')

computegrade(0.5)