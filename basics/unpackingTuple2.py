albums = [("Welcome to my Nightmare","Alice Cooper",1975),
         ("Bad Company","Bad Company",1974),
         ("Nightflight","Budgie",1981),
         ("More Mayhem","Emilda May",2011),
         ("Ride the lightning","Metallica",1984)
         ]

for album in albums:
    Name,Artist,Year = album
    print("Name: {0} \nArtist: {1} \nYear: {2} \n"
          .format(Name,Artist,Year))
    

#Gives same output as above
for Name,Artist,Year in albums:
    print("Name: {0} \nArtist: {1} \nYear: {2} \n"
          .format(Name,Artist,Year))
    
