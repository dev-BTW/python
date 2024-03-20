def factorial(num):
    fact=1
    if num==0:
        return 1
    else:
        for i in range(1,num+1):
            fact*=i
        return fact
    

def recurFactorial(x:int)->int:
    if x<=1:
        return 1
    else:
        return x*factorial(x-1)
    
for i in range(36):
    print(i,factorial(i))   #print(i,recurFactorial(i))


