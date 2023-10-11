# Use a for loop and an if statement to print just the capitals in the following quote.

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
#both code block performs the same task 
uppercase1 =""
uppercase2=""

for i in quote:
    if i.isupper():
        uppercase1+= i+" "
        

for i in quote:
    if not i.islower() and i.isalpha():
        uppercase2+= i+" "

print(uppercase1,"\n",("*")*80,"\n",uppercase2)
