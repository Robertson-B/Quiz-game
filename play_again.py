import type
import sys
import os

def play_again(): # loop to ask the user if they want to play again 
    game_loop = True
    type.type("\u001b[32mDo you want to play again?")
    type.type("\u001b[33m1) \u001b[34mYes")
    type.type("\u001b[33m2) \u001b[34mNo")
    sys.stdout.flush()

    while True:
        play_again = type.typewriter_input("Enter the number of your choice: ")

        if play_again.isdigit() and 1 <= int(play_again) <= 2: # Input validation
            if int(play_again) != 1:
                print("\u001b[34m\u001b[0m", end="")
                os.system('cls||clear') 
                type.type("\u001b[32mThank you for playing!\n\n\n")
                return game_loop == False # Exits the game

            else:
                print("\u001b[34m\u001b[0m", end="")
                return game_loop == True # Continues the game

        else:
            print("\u001b[34m\u001b[0m", end="")
            type.type("\u001b[31;1mInvalid input. Please enter a number between 1 and 2")
            print("\u001b[34m\u001b[0m", end="")