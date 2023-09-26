"""Using all the alphabets as a string create the following slices: 
    create a slice that produce a strings qpo,edcba and last 8 characters in reverse order"""

letters= "abcdefghijklmnopqrstuvwxyz"

print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba 
print(letters[:17:-1]) #last eight characers in reverse i.e zyxwvuts

print("\nUsing negative indexing \n")
#using negative slicing

print(letters[-10:-13:-1]) #qpo
print(letters[-22::-1]) #edcba 
print(letters[:-9:-1]) #last eight characers in reverse i.e zyxwvuts