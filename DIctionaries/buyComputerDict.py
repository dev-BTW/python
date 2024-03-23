availableParts = {
    "1":"Computer",
    "2":"Monitor",
    "3":"Keyboard",
    "4":"Mouse ",
    "5":"HDMI Cable",
    "6":"DVD Drive"
}


currectChoice = None
partsList = []

while currectChoice!='0':
    if currectChoice in availableParts:
        chosenPart = availableParts[currectChoice]
        if chosenPart in partsList:
            #already there so remove it
            partsList.remove(chosenPart)
        else:
            print(f"Adding {chosenPart}") 
            partsList.append(chosenPart)
        print(f"Your list now contains {partsList}")
    else:
        print("Please choose from the available parts below")
        for key,value in availableParts.items():
            print(f"{key}:{value}")
        print("0 to finish")
    currectChoice=input("> ")
