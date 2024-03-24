"""
WAP to count number of time an alphabet is repeated in given text and store them in a dict where key
is the aplhabet and value is the number of time it is repeated
"""
word_count={}

text="Later in the course, you'll see how to use the collections Counter class."

"""
for i in text.casefold():       #.casefold() or .lower()/.upper() to make it case insensitive
    if i.isalnum():
        if i not in word_count:
            word_count[i]=text.count(i)
"""


for i in text.casefold():
    if i.isalnum():
        word_count[i]=word_count.setdefault(i,0)+1  
        #if does not exist create key-value pair and if exists value +1


"""
#does the same thing as above for loop

for i in text.lower():
    if i.isalnum():
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
"""

for key,value in sorted(word_count.items()):
    print(f"{key}:{value}")