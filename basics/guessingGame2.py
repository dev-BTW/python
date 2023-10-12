import random
attempts=1
answer = random.randint(1,10)  #random int within range 1,10 (10 inclusive)
print("Guess a number between 1-10 \nYou got 5 attempts")
while attempts <=5:
    guess = int(input("Attempt no. {0}: ".format(attempts)))
    if (guess>answer):
        print("Please guess lower")
    elif (guess<answer):
        print("Please guess higher")
    else:
        print("You guessed correctly in {0} attempts!!".format(attempts))
        break
    attempts+=1