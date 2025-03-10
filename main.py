# This is the main file that will run the entire program
import pygame # Music
import ask_catagory
import read_json
import intro
import ask_questions
import os


def main():
    os.system('cls||clear') # Clear the console for any system including stupid macs
    file_path = 'questions.json'
    questions_dict = read_json.read_questions(file_path)
    #intro.intro()
    ask_catagory.fetch_catagories(questions_dict)
    ask_catagory.ask_catagory()
    ask_questions.ask_questions(questions_dict)

main()