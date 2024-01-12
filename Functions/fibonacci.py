def fibonacci(n):
    """returns the 'n'th fibonacci numbers"""
    if 0<=n<=1:
        return n
    num1,num2= 1,0
    result =None
    for i in range(n-1):
        result = num1 + num2
        num2 = num1
        num1 = result
    return result

for i in range(36):
    print(i,fibonacci(i))