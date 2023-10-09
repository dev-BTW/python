age = 20

print(f"Tom is {age} years old") #example of 'f string | formatted string' 
#print("Tom is "+ age + "years old") #this will give an error 

print("Tom is %d years old" % age) #string interpolation

#%s for string
#%f for float 

STR = "Value of PI is"
print("%s %f"% (STR, (22/7))) 

print("Value of pi is %60.50f " %(22/7))