for i in range(1,11):
    print("Table of {0}".format(i))
    for j in range(1,13):
        print("{0:2} multiplied by {1:2} is {2:4}".format(i,j,i*j))
    print("_"*40)