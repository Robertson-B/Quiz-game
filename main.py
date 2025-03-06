import csv
import random
import os
import pygame # Music
import threading # A "very simple" way to make a timer
from terminaltexteffects.effects.effect_blackhole import Blackhole # Cool intro text effect

catagories = {
    'General Knowledge': {'s_line': 1, 'e_line': 8,},
    'Classmates': {'s_line': 10, 'e_line': 12,},
    'The inner machinations of my mind': {'s_line': 14, 'e_line': 15,},
}
catagory = "The inner machinations of my mind"

def main():
    os.system('cls||clear') # Clear the console for any system including stupid macs
    file_path = 'questions.csv'
    read_questions(file_path)

def read_questions(file_path):
    questions = []
    # Read questions from the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        score = 0
        for line_number, row in enumerate(csv_reader):
            if catagories[catagory]["s_line"] <= line_number <= catagories[catagory]["e_line"]:  # Specify the line numbers you want to read (1-based index)
                question = row[0]
                correct_answer = row[1]
                wrong_answers = [answer for answer in row[2:] if answer]  # Filter out empty strings
                questions.append((question, correct_answer, wrong_answers))
                random.shuffle(questions) # Shuffle the questions so they aren't in order
                
    # Ask the questions
    for question, correct_answer, wrong_answers in questions: # Why the hell did I do it this way?
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers) # Shuffle the answers so the correct one isn't always last
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



""" This will eventually be an awesome intro to the game
def intro():
    effect = Blackhole("███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗███████╗    ██████╗ ███████╗   ████████╗██╗  ██╗███████╗   ███╗   ███╗██╗███╗   ██╗██████╗ \n██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝   ██╔═══██╗██╔════╝   ╚══██╔══╝██║  ██║██╔════╝   ████╗ ████║██║████╗  ██║██╔══██╗\n███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║███████╗   ██║   ██║█████╗        ██║   ███████║█████╗     ██╔████╔██║██║██╔██╗ ██║██║  ██║\n╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║╚════██║   ██║   ██║██╔══╝        ██║   ██╔══██║██╔══╝     ██║╚██╔╝██║██║██║╚██╗██║██║  ██║\n███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝███████║   ╚██████╔╝██║           ██║   ██║  ██║███████╗   ██║ ╚═╝ ██║██║██║ ╚████║██████╔╝\n╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝    ╚═════╝ ╚═╝           ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ \n==============================================================================================================================================\n\n© 2024 BitRealm Studios. All right reserved.\nCreated by Benjamin Robertson")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("")
"""

main()