#Modify the code so that it stops printing when it reaches a number greater 
#than zero that's exactly divisible by 11.

for i in range(0, 100, 7):
    print(i)
    if i > 0 and  i%11==0:
        break