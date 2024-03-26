vehicles = {
    'dream':'Honda 250T',
    'roadster':'BMW R110',
    'er5':'Kawasaki ER5',
    'can-am':'Bombardier Can-Am 250',
    'virago':'Yamaha XV250',
    'tenere':'Yamaha XT650',
    'jimny':'Suzuki Jimny 1.5',
    'fiesta':'Ford Fiesta Ghia 1.4'
}

#adding value to a dictionary
vehicles['swift'] = 'Suzuki Swift'
vehicles['toy'] = 'Glider'
del(vehicles['swift'])   #delete value from a dict
vehicles['toy']= 'Nissan GTR'  #update a value

#for i in vehicles:
#    print(i,vehicles[i],sep=", ")

for key,values in vehicles.items():
    print(key,values,sep=", ")