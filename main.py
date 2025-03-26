# This is the main file that will run the entire program
import read_json
import intro
import ask_catagory
import ask_questions
import play_again


def main():
    file_path = 'questions.json' # file with questions
    questions_dict = read_json.read_questions(file_path) # sovert json file to one massive dictonary for speed and simplicity
    player_name = intro.intro() 
    while game_loop == True: # Main game loop
        selected_catagory = ask_catagory.ask_catagory(questions_dict)
        ask_questions.ask_questions(questions_dict, player_name, selected_catagory)
        game_loop = play_again.play_again()

if __name__ == "__main__":
    main()