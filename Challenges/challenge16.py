"""WAP a program that will return a deep copy of a dict without using copy module"""

inventory = {
    "Sword":1,
    "Wood":64,
    "Planks":32,
    "Water":6,
    "Lava":2,
    "Glass":13,
    }


def deepCopy(d:dict)->dict:
    copyInventory={}
    for key,value in d.items():
        copyInventory[key]=value
    return copyInventory

newDict = deepCopy(inventory)

newDict["Glass"]=10

#Check both values for glass
print(newDict)
print(inventory)


print(id(newDict))
print(id(inventory))