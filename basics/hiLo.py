low = 1 
high = 1000
guess_count=1

print("Please think of a number between {0} to {1}".format(low,high))
input("Press enter to start")

computers_Guess=1

while True:
    computers_Guess = low+(high-low)//2
    user_Input = input("My answer is {0}.\nPress H or L or C to guess higher ,lower of correct: "
                       .format(computers_Guess)).casefold()
    if user_Input == "h":
        low = computers_Guess
    elif user_Input == "l":
        high = computers_Guess
    elif user_Input=="c":
        print("Yay I guessed it correctly in {0} guesses".format(guess_count))
        break
    else:
        print("please enter H or L or C")
    guess_count += 1