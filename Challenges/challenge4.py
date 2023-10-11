"""Write a program to ask for name and age 
when both values are entered, check if the person is the right age to go on on 18-30 holidy
(they must be over 18 and under 31)"""

name = str(input("What's your name?"))
age = int(input("what's your age? "))


if name != "" and age != None:
    if 18 <= age < 31:
        print("Enjoy your holiday {0}".format(name))
    elif age < 18:
        print("{0} you're eligible for holiday after {1} years".format(name,(19-age)))
    else:
        print("{0} you're {1} years older for holiday".format(name,(age-31)))