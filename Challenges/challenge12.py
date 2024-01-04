"""For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
The user input is of the form: a,b,c, where a, b and c are numbers."""

numbers = input("Enter three numbers separated by ',': ")

numbers_list = numbers.split(",")
#print(numbers_list)

for i in range(len(numbers_list)):   #convert string to int
    numbers_list[i] = int(numbers_list[i]) 

#print(numbers_list)
print(numbers_list[0]+numbers_list[1]-numbers_list[2])