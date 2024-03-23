from contents import pantry

chickenQuantity = pantry.setdefault("chicken",0)
print(f"Chicken: {chickenQuantity}")


#diference between .setdefault and .get method


beansQuantity = pantry.setdefault("beans",0)   #.setdefault()
print(f"Beans: {beansQuantity}")

ketchupQuantity = pantry.get("ketchuhp",0)      #.get()
print(f"Ketchup: {ketchupQuantity}")


for key,value in pantry.items():
    print(f"{key}:{value}")