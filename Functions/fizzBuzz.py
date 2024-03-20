
def fizzBuzz(num:int)->str:
    """
    Fizz Buzz
    :param num: Number to check
    :returns: "fizz" if number is divisible by 3 
        "buzz" if divisible by 5
        "fizz buzz" if divisible by both
        returns the number as string otherwise 
    """

    if num%3==0 and num%5==0:
        return "fizz buzz"
    elif num%3==0:
        return "fizz"
    elif num%5==0:
        return "buzz"
    else:
        return str(num)
        
i = 0 
while i<99:
    i+=1
    print(fizzBuzz(i))

    i+=1
    correctGuess=fizzBuzz(i)
    userGuess = str(input("Your Go: "))
    if (userGuess!=fizzBuzz(i)):
        print("You lose the correct answer was ",correctGuess)
        break
else:
    print("You Won!!")

"""
#does the same thing as above while loop

for i in range(1,101):
    print("current Number: ",i)
    if (i%2==0):
        print(fizzBuzz(i))
    else:
        playersChoice=str(input())
        if(playersChoice!=fizzBuzz(i)):
            print("You lose")
            break

"""