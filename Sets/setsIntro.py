#Creating a Set

#running the code several times will show that sets prints in random order
#we can iterate over a set but the order will change everytime you run the code
#hence indexing a set is not possible

farmAnimals = {'Cow','Sheep','Hen','Goat','Horse'}
print(farmAnimals)      
moreAnimals={'Sheep','Goat','Cow','Horse','Hen'}

if moreAnimals==farmAnimals:
    print("Equal sets")
else:
    print("Sets are different")