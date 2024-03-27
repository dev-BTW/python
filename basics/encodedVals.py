#.encode('utf8') translates unicode character to its respective value
string="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
#blank spaces are line break or space 
for i in string.encode('utf8'):
    print(f"{i} ---> {chr(i)}")

print(string.encode('utf8'))