def example(a,b,*args,c,**kwargs):
    print("Positional {}{}".format(a,b))
    print("Variable values {}".format(*args))
    print("Use keyword {}".format(c))
    print("Valiable keyword {}".format(kwargs))


example(1,2,3,4,5,c=16,key1=21,key2=22)  #we need to use the key value 'c' to specify its value