answer = 5

print("Please Guess a number between 1 to 10: ")
guess = int(input())


if guess<answer:
    print("Please guess higher")

elif guess > answer:
    print("Please guess lower")

else:
    print("Guessed correctly")