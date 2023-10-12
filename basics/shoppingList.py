shopping_List = ["milk","pasta","ketchup","rice","wheat"]

for item in shopping_List:
    print("Buy "+ item)

print("_"*40)

for item in shopping_List:
    if item!="pasta":           #exclude pasta
        print("Buy "+ item)

print("_"*40)

#another method to exclude pasta 

for item in shopping_List:
    if item == "pasta":
        continue                        #use to skip a code block for specified iterations
    
    else:
        print("Buy "+ item)