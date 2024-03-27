data = [
    ("orange","Sweet orange fruit,citrus fruit"),
    ("apple","Red fruit, good for making cider"),
    ("lemon","Sour,yellow citrus fruit"),
    ("grape","small,sweet,grows in bunch"),
    ("melon","Sweet and juicy")
]

def simpleHash(X:str)->int:
    basicHash = ord(X[0])      #X[0] returns the first character of value of X
    return(basicHash%10) 

keys =[""]*10   #created an empty list
values = keys.copy()

#The below code maps checks the hash and maps the key-value pair to the index position of both list

for key,value in data:
    h=simpleHash(key)
    print(key,h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)