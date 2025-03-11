# This is the main file that will run the entire program
import ask_catagory
import read_json
import intro
import ask_questions
import os
import music

def main():
    file_path = 'questions.json'
    questions_dict = read_json.read_questions(file_path)
    #intro.intro()
    #music.main_music()
    play_game(questions_dict)


def play_game(questions_dict):
    while True:
        os.system('cls||clear') # Clear the console for any system including stupid macs
        ask_catagory.ask_catagory(questions_dict)
        ask_questions.ask_questions(questions_dict)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break


main()