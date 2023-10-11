activity = input("What would you like to do today? ")

#.casefold() is used for caseless matching of strings
if "python" not in activity.casefold():
    print("Should learn python today")