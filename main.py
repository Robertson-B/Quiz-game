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
    #intro.intro()
    #music.main_music()
    play_game(questions_dict)


def play_game(questions_dict):
    game_loop = True
    while game_loop == True:
        os.system('cls||clear') # Clear the console for any system including stupid macs
        ask_catagory.ask_catagory(questions_dict)
        ask_questions.ask_questions(questions_dict)
        type.type("Do you want to play again?")
        type.type("1) Yes")
        type.type("2) No")
        sys.stdout.flush()
        while True:
            play_again = type.typewriter_input("Enter the number of your choice: ")
            if play_again.isdigit() and 1 <= int(play_again) <= 2:
                play_again = int(play_again)
                if play_again != 1:
                    print("\u001b[34m\u001b[0m", end="")
                    os.system('cls||clear') # Clear the console for any system including stupid macs
                    type.type("Thank you for playing!\n\n\n")
                    game_loop = False
                    break
                else:
                    print("\u001b[34m\u001b[0m", end="")
                    break
            else:
                print("\u001b[34m\u001b[0m", end="")
                type.type("Invalid input. Please enter a number between 1 and 2")

if __name__ == "__main__":
    main()