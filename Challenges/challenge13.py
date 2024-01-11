"""Write a program with function 'sum_eo' with parameters n (a +ve number),t(a string)
If t have the value 'e' then the program should return sum of all even natural number less than n
If t have value o then sum of odd numbers till n 
For other value of t return -1
"""

def sum_EO(n,t):
    t=t.lower()
    if t=='e':
        i=2
    elif t=='o':
        i=1
    else:
        return-1

    return sum(range(i,n,2))


print(sum_EO(10,'E'))
print(sum_EO(9,'o'))
print(sum_EO(15,'O'))
print(sum_EO(16,'e')) 

