import csv
import random
import os
import pygame # Music
import threading # A "very simple" way to make a timer
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect

catagories = {
    'General Knowledge': {'start_line': 1, 'end_line': 8,},
    'Classmates': {'start_line': 10, 'end_line': 12,},
    'The inner machinations of my mind': {'start_line': 14, 'end_line': 15,},
    'Star Wars': {'start_line': 17, 'end_line': 25,}
}
catagory = "Star Wars"

def main():
    os.system('cls||clear') # Clear the console for any system including stupid macs
    file_path = 'questions.csv'
    questions_dict = read_questions(file_path)
    ask_questions(questions_dict)

def read_questions(file_path):
    questions_dict = {}
    # Read questions from the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for line_number, row in enumerate(csv_reader):
            for category, lines in catagories.items():
                if lines["start_line"] <= line_number <= lines["end_line"]:
                    if category not in questions_dict:
                        questions_dict[category] = []
                    question = {
                        'question': row[0],
                        'correct_answer': row[1],
                        'wrong_answers': [answer for answer in row[2:] if answer]  # Filter out empty strings
                    }
                    questions_dict[category].append(question)
    return questions_dict

def ask_questions(questions_dict):
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

    if score == len(questions):
        print(f'\nYour final score is: {score}/{len(questions)}')
        print('Congratulations! You got all the questions right!\n\n\n')
    else:
        print(f'\nYour final score is: {score}/{len(questions)}')
        print('Better luck next time!\n\n\n')

def intro(): # This is the intro text effect
    os.system('cls||clear') # Clear the console for any system including stupid macs
    effect = Blackhole(" ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝\n=======================================================================\n\n© 2024 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")

main()