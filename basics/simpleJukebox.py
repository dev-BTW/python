from simpleJukeboxData import Albums
songIndex = 3
songTitleIndex = 1

while True:
    for Index,(Title,Artist,Year,Songs) in enumerate(Albums):
        print("{0}>> Title: {1} Artist: {2} Year: {3}".format(Index+1,Title,Artist,Year))

    Choice1 = int(input("Select an Album: "))
    if (1<= Choice1<= len(Albums)):
        songList = (Albums[Choice1-1][songIndex])
    else:
        break
    for Index,(trackNumber,Song) in enumerate(songList):
        print("{0}>>> Song: {1}".format(Index+1,Song))
    Choice2 = int(input("Select a song:"))
    if (1<= Choice2 <= len(songList)):
        print("Playing {0}".format(songList[Choice2-1][songTitleIndex]))
        print("="*40)
    

    