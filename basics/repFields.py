age = 20

#print("My age is " + age + " years") will throw error because int cannot be  concatenated with a string
print("My age is " + str(age) + " years")

#replacement field is represented by {0} and it is replaced by the first value in the format list
print("My age is {0} years".format(age)) 

print("There are {0} days in {1}, {2} ,{3} ,{4} ,{5} ,{6} ,and {7}"
      .format(31,"Janauary","March","May","July","August","October","December"))

"""In the above code we used 8 replacement fields numbered 0-7.
Each """

print("Jan:{2} ,Feb:{0} ,Mar:{2} ,Apr:{1} ,May:{2} ,Jun:{1} ,Jul:{2} ,Aug:{2} ,Sept:{1} ,Oct:{2} ,Nov:{1} ,Dec:{2}"
      .format(28,30,31)) 