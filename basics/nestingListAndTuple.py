#Nested list 

Numbers = [
    ["Even",[2,4,6,8,10]],
    ["Odd",[1,3,5,7,9]]
]

print(Numbers)
print(Numbers[0])
print(Numbers[1])

print(Numbers[0][0])
print(Numbers[0][1][1:])
print(Numbers[0][1][:3])


#Nested Tuple

Subjects = (
    ("Science",(1,2,3,4,5)),
    ("Maths",(1,2,3,4,5,6,7))
)

print(Subjects)
print(Subjects[0])
print(Subjects[1])

print(Subjects[0][1][2])