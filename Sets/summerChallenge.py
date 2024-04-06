choice ="~"

while choice!="0":
    if choice in set('12345'):
        print(f"You chose {choice}")
    else:
        print("Select from the following items")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tRead a book")
        print("5:\tPlay Cricket")
        print("0:\tExit")


    choice=input()