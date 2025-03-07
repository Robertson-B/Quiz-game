import json
import random
import os
import pygame # Music
import threading # A "very simple" way to make a timer
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect

catagories = {}
catagory = ""

def main():
    os.system('cls||clear') # Clear the console for any system including stupid macs
    file_path = 'questions.json'
    questions_dict = read_questions(file_path)
    fetch_catagories(questions_dict)
    ask_catagory()
    ask_questions(questions_dict)

def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions_dict = json.load(file)
    return questions_dict

def fetch_catagories(questions_dict):
    global catagories
    catagories = {category: questions for category, questions in questions_dict.items()}

def ask_questions(questions_dict): # Asks the questions
    questions = questions_dict[catagory]
    random.shuffle(questions)
    score = 0

    for question_data in questions:
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        wrong_answers = question_data['wrong_answers']
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers)
        print(question)
        for i, answer in enumerate(answers):
            print(f'{i + 1}) {answer}') # This was fun to figure out how to do

        while True: # Makes sure the input is valid
            user_answer = input('Enter the number of the correct answer: ').strip()
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                break
            else:
                print('Invalid input. Please enter a number between 1 and', len(answers))

        if answers[int(user_answer) - 1] == correct_answer: # Because lists start at zero not one
            score += 1
            print('\nCorrect!\n')
        else:
            print(f'\nWrong! The correct answer was: {correct_answer}\n')

    if score == len(questions): # Print user score
        print(f'\nYour final score is: {score}/{len(questions)}')
        print('Congratulations! You got all the questions right!\n\n\n')
    else:
        print(f'\nYour final score is: {score}/{len(questions)}')
        print('Better luck next time!\n\n\n')

def intro(): # This is the intro text effect
    os.system('cls||clear') # Clear the console for any system including stupid macs
    effect = Blackhole(" ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\n======================================================================\n\n© 2024 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")

def ask_catagory(): # Asks the user to select a catagory
    global catagory
    print("Please select a catagory:")
    for i, catagory_name in enumerate(catagories.keys(), 1):
        print(f'{i}) {catagory_name}')
    while True:   # Makes sure the input is valid
        user_input = input('Enter the number of the catagory: ').strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(catagories):
            print("")
            break
        else:
            print('Invalid input. Please enter a number between 1 and', len(catagories))
    catagory = list(catagories.keys())[int(user_input) - 1]

main()