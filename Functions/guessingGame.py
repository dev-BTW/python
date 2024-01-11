import random
min = 1
max = 100
answer = random.randint(min,max)
print(answer)

def getNumber():
    guess=0   
    guess = input("Guess a number between {} and {}: ".format(min,max))
    if guess.isnumeric():
        guess = int(guess)
        return validate(guess)
    else:
        print("{} is not a valid number".format(guess))
        getNumber()


def validate(num):
    while True:
        if num > answer:
            print("Guess Lower")
            getNumber()
        elif num < answer:
            print("Guess Higher")
            getNumber()
        else:
            print("Correct Guess!!!")
        break
    

getNumber()