import copy

animals={
    "Lion":"Scary",
    "Elephant":"Big",
    "Teddy":"Cuddly"
}


#Creates a deep copy or a separate dict 
things = copy.deepcopy(animals)
things["Teddy"]="Toy"

print(things)  #does not affect the original list
print(animals)

#to confirm both dicts are not sharing the same reference
print(id(things))  
print(id(animals))
