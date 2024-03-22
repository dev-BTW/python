numbers = (0,1,2,3,4,5,6,7)

print(numbers)
print(*numbers,sep=";") #unpacks values 
print(0,1,2,3,4,5,6,7,sep=";")


def testStar(*args):        #multiple or no parameter can be passed  
    print(args)
    for i in args:
        print(i)

testStar(0,1,2,3,4,5,6)