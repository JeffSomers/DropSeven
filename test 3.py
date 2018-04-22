def geef (x,y=None):

    if y == None:
        y = 7

    elif x <7:
        return 1 + geef(x-1)


print(geef(2))