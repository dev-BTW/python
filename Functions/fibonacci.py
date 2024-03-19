def fibonacci(n):
    if 0<=n<=1:
        return n
    num1,num2=1,0

    for i in range(n-1):
        result = num2+num1 
        num2 = num1
        num1 = result

    return result
for i in range(10):
    print(i,fibonacci(i))  