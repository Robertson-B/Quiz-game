# This is the main file that will run the entire program
import ask_catagory
import read_json
import intro
import ask_questions
import os
import music
import type
import sys 


def main():
    file_path = 'questions.json'
    questions_dict = read_json.read_questions(file_path)
    player_name = intro.intro()
    #music.main_music()
    play_game(questions_dict, player_name)


def play_game(questions_dict, player_name):
    game_loop = True
    while game_loop == True:
        os.system('cls||clear') # Clear the console for any system including stupid macs
        ask_catagory.ask_catagory(questions_dict)
        ask_questions.ask_questions(questions_dict, player_name)
        type.type("\u001b[32mDo you want to play again?")
        type.type("\u001b[33m1) \u001b[34mYes")
        type.type("\u001b[33m2) \u001b[34mNo")
        sys.stdout.flush()
        while True:
            play_again = type.typewriter_input("Enter the number of your choice: ")
            if play_again.isdigit() and 1 <= int(play_again) <= 2:
                play_again = int(play_again)
                if play_again != 1:
                    print("\u001b[34m\u001b[0m", end="")
                    os.system('cls||clear') # Clear the console for any system including stupid macs
                    type.type("\u001b[32mThank you for playing!\n\n\n")
                    game_loop = False
                    break
                else:
                    print("\u001b[34m\u001b[0m", end="")
                    break
            else:
                print("\u001b[34m\u001b[0m", end="")
                type.type("'\u001b[31;1mInvalid input. Please enter a number between 1 and 2")
                print("\u001b[34m\u001b[0m", end="")

if __name__ == "__main__":
    main()