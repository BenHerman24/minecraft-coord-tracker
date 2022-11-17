from Chest import Chest

mainChest = Chest(3456)

inputSetBuffer = Chest(0)
inputCoordBuffer = Chest(0)
outputMovementBuffer = Chest(0)

wantedCoord = 0

print("all inputs are numbers")
realCoord = int(input("where are you: "))
oldWantedCoord = realCoord

while True:

    # setup
    wantedCoord = int(input("where do you want to go: "))
    if oldWantedCoord < wantedCoord:
        inputSetBuffer.items = wantedCoord - oldWantedCoord
    if oldWantedCoord > wantedCoord:
        mainChest.removeItems(oldWantedCoord - wantedCoord)
    oldWantedCoord = wantedCoord
    

    while realCoord != wantedCoord:
        if not mainChest.isFull():
            realCoord -= 1
            # because of the movement
            inputCoordBuffer.addItems(1)

        if not outputMovementBuffer.isEmpty():
            realCoord += 1
            # because of the movement
            outputMovementBuffer.removeItems(1)
            
        if not inputCoordBuffer.isEmpty():
            if mainChest.isFull():
                if not outputMovementBuffer.isFull():
                    inputCoordBuffer.removeItems(1)
                    outputMovementBuffer.addItems(1)
            else:
                inputCoordBuffer.removeItems(1)
                mainChest.addItems(1)

        if not inputSetBuffer.isEmpty():
            if mainChest.isFull():
                if not outputMovementBuffer.isFull():
                    inputSetBuffer.removeItems(1)
                    outputMovementBuffer.addItems(1)
            else:
                inputSetBuffer.removeItems(1)
                mainChest.addItems(1)
        
        input("-----------")
        print(realCoord)
        print(mainChest.items, mainChest.isFull())
        print(outputMovementBuffer.items)
        print(inputCoordBuffer.items)
        print(inputSetBuffer.items)