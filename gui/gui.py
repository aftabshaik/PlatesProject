import os
import sys
from functions import stacker


### added to properly clear console at start of program 
### needed to account for OS type of user               
if sys.platform in ('linux', 'darwin'):
    CLEAR = "clear"
elif sys.platform == 'win32':
    CLEAR = "cls"
else:
    print(f"User System {sys.platform} not supported, ")
    print("console will not be cleared during option select.")
    CLEAR = ""

# Used to clear console for new gui draw
def clear():
    os.system(CLEAR)

### start menu GUI ###
def printMenu():
    clear()
    print("")
    print("===========================================================")
    print("|            Plate Stacker by Aftab Shaik                 |")
    print("===========================================================")
    print("| Please choose an option (1-4) from the list below:      |")
    print("|                    1. Add a Plate                       |")
    print("|                    2. Remove Plates                     |")
    print("|                    3. Print your Plate Stack            |")
    print("|                    4. Quit                              |")
    print("===========================================================")
    print("")
    optionSelected = input("Please select an option: ")
    guiNavigation(inputCleanUp(optionSelected))
    return 

# Menu after plates added #
def postPrintMenu():
    if stacker.numericPlateStack == []:
        print("")
        print(f"You are not holding any plates!")
    else:
        print("")
        print(f"You currently have {len(stacker.numericPlateStack)} plate(s) in your stack.")
        print(f"Your current plate stack is: {stacker.numericPlateStack} ")
    print("")
    print("===========================================================")
    print("| Please choose an option (1-4) from the list below:      |")
    print("|                    1. Add a Plate                       |")
    print("|                    2. Remove Plates                     |")
    print("|                    3. Print your Plate Stack            |")
    print("|                    4. Quit                              |")
    print("===========================================================")
    print("")
    optionSelected = input("Please select an option: ")
    guiNavigation(inputCleanUp(optionSelected))

# case matching and string to int conversion for option selection
def inputCleanUp(data):
    match data:
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case "4":
            return 4
        case _:
            return 0

def guiNavigation(option):
    option = int(option)
    if option == 1:
        clear()
        print(f"Your current plate stack is: {stacker.numericPlateStack} ") # Implemented catch statement here to ensure program doesn't error out
        newPlate = input("What size plate do you want to add? ")            # when user enters none integer values into plate addition function.
        try: 
            stacker.addPlate(int(newPlate))
            postPrintMenu()
        except:
            print(f"Your input {newPlate} is not an integer. No plates added!")
            postPrintMenu()
    elif option == 2:
        clear()
        print(f"Your current plate stack is: {stacker.numericPlateStack} ") # Implemented catch statement here to ensure program doesn't error out   
        howManyToRemove = input("How many plates do you want to remove? ")  # when user enters none integer values into plate removal function
        try:
            stacker.remPlate(int(howManyToRemove))
            postPrintMenu()
        except:
            print(f"Your input {howManyToRemove} is not an integer. No plates removed!")
            postPrintMenu() 
    elif option ==3:
        clear()
        stacker.showPlateStack()
        postPrintMenu()
    elif option == 4:
        exit
    elif option is 0:
        print(f"You didn't choose any option! Please choose a valid option.")
        postPrintMenu()