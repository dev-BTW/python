parrot = "Norwegin Blue"
separators =""

for i in parrot:
    print(i)

numbers = "9,12,32,322,13,231,1,1331,13"

for i in numbers:
    if not i.isnumeric():
        separators += i

print(separators)