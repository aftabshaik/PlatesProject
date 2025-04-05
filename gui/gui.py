import os
import sys
from functions import stacker


### added to properly clear console at start of program ###
### needed to account for OS version of user            ###
if sys.platform in ('linux', 'darwin'):
    CLEAR = "clear"
elif sys.platform == 'win32':
    CLEAR = "cls"
else:
    print(f"User System {sys.platform} not supported, console will not be cleared.")
    CLEAR = ""

def clear():
    os.system(CLEAR)

### start menu GUI ###
def printMenu():
    clear()
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
    clear()
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
        newPlate = input("What size plate do you want to add? ")
        stacker.addPlate(int(newPlate))
        postPrintMenu()
    elif option == 2:
        howManyToRemove = input("How many plates do you want to remove? ")
        stacker.remPlate(int(howManyToRemove))
        postPrintMenu()
    elif option ==3:
        postPrintMenu()
    elif option == 4:
        postPrintMenu()
    elif option is 0:
        postPrintMenu()




def visualPlateStacker(plateStack):
    for n in plateStack:
        print(f"-" * n)
    