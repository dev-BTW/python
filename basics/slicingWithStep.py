"""
N -14 or 0
o -13 or 1
r -12 or 2
w -11 or 3
e -10 or 4
g -9 or 5
i -8 or 6
a -7 or 7
n -6 or 8
  -5 or 9
B -4 or 10
l -3 or 11
u -2 or 12
e -1 or 13
"""

parrot = "Norwegian Blue"
number = "123456789"
#syntax:- parrot[start index : end index : step]  
#if step is 1 then it'll print very next character to current character 
#if step is 2 then it'll print character which is 2 index position apart 


#print(parrot[0:10:2])

print(number[::1]) #123456789
print(number[::2]) #13579
print(number[1::2]) #2468
print(number[0:6:3]) #14
print(number[5::3]) 