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

#provided key returns value
myCar = vehicles['roadster']
print(myCar)
commuter = vehicles.get('er5')
print(commuter)