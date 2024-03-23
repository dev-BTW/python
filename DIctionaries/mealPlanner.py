from contents import *

displayDict = {}
shoppingList = {} 

def updateShoppinfList(Items:str ,Quantity:int) -> None:
    if Items in shoppingList:
        shoppingList[Items]+=Quantity
    else:
        shoppingList[Items]=Quantity


for index,key in enumerate(recipes):
    displayDict[str(index+1)] = key

while True:
    print("Choose a meal")
    for key,value in displayDict.items():
        print(f"{key}:{value}")

    choice = input("> ")

    if choice == "0":
        break
    elif choice in displayDict:
        selectedItem = displayDict[choice]
        print(f"You have selected {selectedItem}")
        print("Checking INgredients")
        ingredients = recipes[selectedItem]
        for foodItem, requiredQuantity in ingredients.items():
            quatityInPantry = pantry.get(foodItem,0)
            if requiredQuantity <= quatityInPantry:
                print(f"{foodItem} OK")
            else:
                quantityToBuy = requiredQuantity-quatityInPantry
                print(f"You need to buy {quantityToBuy} of {foodItem}")
                print("Updating Shopping List")
                updateShoppinfList(foodItem,quantityToBuy)
                
for food,quant in shoppingList.items():
    print(f"Buy {food}--->{quant}")
