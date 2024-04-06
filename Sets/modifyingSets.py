#A set cannot contain duplicate items
numbers=set()

print(numbers,type(numbers))
while len(numbers)<4:
    val=int(input("Enter your next value: "))
    numbers.add(val)

print(numbers) 

#removing duplicate values from data

data = ["blue","green","blue","red","blue","black","red","purple"]

uniiqueSet = set(data) #set contains unique element
#to order a set you can use sorted function
sortedSet = sorted(uniiqueSet) #or sorted(set(data))
print(uniiqueSet) 
print(sortedSet) #this set will print in same order since it is sorted

#create list of unique colours 
uniqueData = list(dict.fromkeys(data))  #removes duplicate data
print(uniqueData)