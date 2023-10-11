parrot = "Norwegian Blue"

letter = str(input("Enter character: "))

if letter in parrot:
    print("{0} is in {1}".format(letter,parrot))
else:
    print("{0} is not {1}".format(letter,parrot))