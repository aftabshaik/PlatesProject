
numericPlateStack = []

# adds plates to stack
# if stack is empty, appends
# if stack exists, adds plate to start of the stack if size less than plate
# at index 0 
def addPlate(numbPlate):
    if numbPlate < 1 :
        return print("Cannot add a plate with size less than 1.")
    if numericPlateStack == []:
        numericPlateStack.append(numbPlate)
    elif numericPlateStack[0] >= numbPlate:
        numericPlateStack.insert(0,numbPlate)
    else:
        print(f"Cannot add plate size {numbPlate} above plate size {numericPlateStack[0]}")

# removes plates, starting from index 0 of list,
# checks for length of passed value as non zero positive integer less than length of list
# catches errors as well.
def remPlate(numberOfPlates):
    if 0 < numberOfPlates and numberOfPlates <= len(numericPlateStack):
        del numericPlateStack[0:numberOfPlates]
    elif numberOfPlates > len(numericPlateStack):
        return print(f"Cannot remove more plates than {len(numericPlateStack)}!")
    elif numberOfPlates == 0:
        return print("Cannot remove zero plates!")
    elif numberOfPlates < 0:
        return print(f"Cannot remove {numberOfPlates} plates!")

# prints plate stack using ascii art
# plate stack is drawn using join statements and centered for eye candy
def showPlateStack():
    print("")
    print(f"Your current stack of plates: {numericPlateStack}")
    if numericPlateStack == []:
        print(f"Cannot visualize empty stack of plates.")
        print("")
    else:
        print("Let's visualize this:")
        print("")
        for n in numericPlateStack:

            visualPlateStack = ["="]*n
            centeredPlates = "".join(visualPlateStack)
            print(centeredPlates.center(numericPlateStack[len(numericPlateStack)-1]))

        print("\/".center(numericPlateStack[len(numericPlateStack)-1]))
        print("||".center(numericPlateStack[len(numericPlateStack)-1]))
        print("||".center(numericPlateStack[len(numericPlateStack)-1]))
    