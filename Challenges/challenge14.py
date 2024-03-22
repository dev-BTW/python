"""Write a function to calculate the sum of all numbers passed as its arguments."""

def sum_numbers(*args:float)->float:
    result = 0
    for i in args:
        result+=i
    return result

def builtInSum(*vals:float)->float:
    return sum(vals)

print(sum_numbers(1,2,3))
print(builtInSum(2,4,6,8))