name = str(input("Enter your name: "))
age = int(input("Enter your age {0}: ".format(name)))


if age < 18:
    print("You can vote after {0} years".format(18-age))


elif age == 900:
    print("Why are you still alive!!!")

else:
    print("You're old enough to vote")

