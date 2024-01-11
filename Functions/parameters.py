1#here a and b are two parameters
def multiply(a,b):
    return a*b
# parameters--->(a,b)
print(multiply(2,5))  #2 and 5 are arguments


for i in range(1,11):
    print("2 times {0}  is equals to {1}"
          .format(i,multiply(2,i)))