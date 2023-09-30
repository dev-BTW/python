for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i,i*i,i*i*i))  #.format(i,i**2,i**3) is same 


for i in range(1,13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i*i,i*i*i))  
    #{0:2} here 2 is field width 
    #so that the replacement field will fill width of 2 and is mostly used to make our results more presentable 


for i in range(1,13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i,i*i,i*i*i)) 
    #{1:<4} 4 is used to specify field width and '<' is used to left align the replacement text|char
    # By default the text is right aligned

for i in range(1,13):
    print("No. {0:2} squared is {1:^4} and cubed is {2:^4}".format(i,i*i,i*i*i)) 
    #{1:<4} 4 is used to specify field width and '^' is used to centre align the text


print("Value of pi is approximately {0:12}".format(22/7))
print("Value of pi is approximately {0:50.54f}".format(22/7)) #50 width and decimal value precision of 54

"""
{0:4} used for specifying field width and right align text
{0:<4} used for left align
{0:^4} used for centre align
"""
