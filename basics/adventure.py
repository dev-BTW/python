available_exits = ["east","west","north","south"]

chosen_exit =""

while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over!!")
        break

print("Gald you made out of there!")