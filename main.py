# This is the main file that will run the entire program
import ask_catagory
import read_json
import intro
import ask_questions
import os
import play_again


def main():
    file_path = 'questions.json'
    questions_dict = read_json.read_questions(file_path)
    player_name = intro.intro() # if 
    game_loop = True
    while game_loop == True:
        os.system('cls||clear') # Clear the console for any system including stupid macs
        ask_catagory.ask_catagory(questions_dict)
        ask_questions.ask_questions(questions_dict, player_name)
        game_loop = play_again.play_again()

if __name__ == "__main__":
    main()