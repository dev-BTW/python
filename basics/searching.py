shopping_List = ["milk","pasta","ketchup","rice","wheat"]
print(shopping_List)

tofind = input("Item to find: ")
found_at = None
print(len(shopping_List))

for indexPos in range(len(shopping_List)):
    if shopping_List[indexPos] == tofind:
        print("Found {0} at index position {1}".format(shopping_List[indexPos],indexPos))
        break
    else:
        continue 