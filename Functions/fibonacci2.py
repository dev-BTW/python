#function annotation and type hints  
def fibonacci(n:int) -> int: 
    if n <=0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range(26):
    print(i,fibonacci(i))