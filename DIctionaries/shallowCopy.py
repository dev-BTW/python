#Demonstration of .copy() method

animals={
    "Lion":"Scary",
    "Elephant":"Big",
    "Teddy":"Cuddly"
}

cars = {
    "BMW":["Fast","Costly"],
    "Audi":["Comfort","Costly"],
    "Toyota":["Fast","Reliable"]
}

things = animals
newThings = animals.copy()  #Creates a shallow copy (coppies reference to the value) of the original dict


animals["Teddy"]="Toy"   #Both animals and things refer to same dict
print(things["Teddy"])
print(animals["Teddy"])
print(newThings["Teddy"])

#Changes to copy will also affect the original dict
#This example uses cars dict

cpyCar = cars.copy()

print(f"Original List {cars}")
print(60*"~")

cpyCar["Toyota"].append("Cheap")
print(cpyCar["Toyota"])     #prints value for toyota from copied dict
print(cars["Toyota"])       #prints value for toyota from Original dict