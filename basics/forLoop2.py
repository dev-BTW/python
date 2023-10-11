numbers = input("Enter several numbers using any separators: ")

separator=""

for i in numbers:
    if not i.isnumeric():
        separator += i

print(separator)