# This is the main file that will run the entire program
import read_json
import intro
import ask_category
import ask_questions
import play_again
import time

def main():
    file_path = 'questions.json' # file with questions
    questions_dict = read_json.fetch_questions(file_path) # covert json file to one massive dictonary for speed and simplicity
    player_name = intro.intro() 
    game_loop = True
    while game_loop == True: # Main game loop
        selected_catagory = ask_category.ask_category(questions_dict)
        ask_questions.ask_questions(questions_dict, player_name, selected_catagory)
        game_loop = play_again.play_again()

if __name__ == "__main__":
    main()