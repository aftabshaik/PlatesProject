import os
import sys



if sys.platform in ('linux', 'darwin'):
    CLEAR = "clear"
elif sys.platform == 'win32':
    CLEAR = "cls"
else:
    print(f"User System {sys.platform} not supported, console will not be cleared.")
    CLEAR = ""


def printMenu():
    os.system(CLEAR)
    print("===========================================================")
    print("|            Plate Stacker by Aftab Shaik                 |")
    print("===========================================================")
    print("| Please choose an option (1-4) from the list below:      |")
    print("|                    1. Add a Plate                       |")
    print("|                    2. Remove a Plate                    |")
    print("|                    3. Print your Plate Stack            |")
    print("|                    4. Quit                              |")
    print("===========================================================")
    print("")
    optionSelected = input("Please select an option: ")
    return optionSelected

def visualPlateStacker(plateStack):
    for n in plateStack:
        