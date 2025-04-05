
numericPlateStack = []


def addPlate(numbPlate):
    if numericPlateStack == []:
        numericPlateStack.append(numbPlate)
        print(numericPlateStack)
    elif numericPlateStack[0] >= numbPlate:
        numericPlateStack.insert(0,numbPlate)
    else:
        print(f"Cannot add plate size {numbPlate} above plate size {numericPlateStack[0]}")
    


def remPlate(numberOfPlates):
    if 0 < numberOfPlates and numberOfPlates <= len(numericPlateStack):
        del numericPlateStack[0:numberOfPlates]
    elif numberOfPlates > len(numericPlateStack):
        print(f"Cannot remove more plates than {len(numericPlateStack)}!")
    elif numberOfPlates == 0:
        print("Cannot remove zero plates!")
    elif numberOfPlates < 0:
        print(f"Cannot remove {numberOfPlates} plates!")

def showPlateStack():
    print(numericPlateStack)