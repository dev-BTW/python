d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

d2={
    7:"Lucky Seven",
    10:"Ten",
    3:"This is the new Three"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

#Using dictionary class to call fromkeys method
#Used to create a dictionary from a list
#if the default value if left empty then the default value would be None for all keys
new_dict = dict.fromkeys(pantry_items,0) #0 is default value
print(new_dict)

Keys = d.keys()       #Returns the keys of specified dict in form of a list
print(Keys)

Values = d.values()  #Returns all the values of dict
print(Values)

print(40*"~")

d.update(d2)  #Appends keys if doesn't exist or Updates values of existing key based on new dict
for key,val in d.items():
    print(f"{key}:{val}")