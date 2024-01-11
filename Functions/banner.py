def banner(text):
    screenWidth = 80

    if len(text) > screenWidth:
        print("Too large for screen")
    
    elif (text=="*"):
        print(text*screenWidth)
    else:
        print("**{}**".format(text.center(screenWidth-4)))

#Random essay
banner("*")
banner("Don't fear the cracks, for they bloom with unseen light. ")
banner("Embrace the broken, for beauty whispers in the night")
banner("Scars tell stories, etched in resilience and grace.")
banner("From shattered pieces, mosaics find their place.")
banner("Dance with the edges, where strength and freedom meet.")
banner("In brokenness, find healing, and make your life complete.")
banner("*")