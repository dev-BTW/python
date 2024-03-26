from contents import pantry

chickenQuantity = pantry.setdefault("chicken",0)
print(f"Chicken: {chickenQuantity}")


#diference between .setdefault and .get method
"""
The .setdefault() method returns value of Key exist,else it create a key value pair with the specified
key and value 
Syntax --->  dictName.setdefault("key",default value)

The .get() method returns value if key exists,else returns the other specified return value.It does not
create a key value pair
Syntax ---> dictName.get("Key",returnValue)
"""

beansQuantity = pantry.setdefault("beans",0)   #.setdefault()
print(f"Beans: {beansQuantity}")

ketchupQuantity = pantry.get("ketchuhp",0)      #.get()
print(f"Ketchup: {ketchupQuantity}")

print()

#The Output would contain key value pair for beans but not for ketchup

for key,value in sorted(pantry.items()):
    print(f"{key}:{value}")