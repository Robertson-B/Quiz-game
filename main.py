import csv
import random
import os

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
        for row in csv_reader:
            question = row[0]
            correct_answer = row[1]
            wrong_answers = [answer for answer in row[2:] if answer]  # Filter out empty strings
            questions.append((question, correct_answer, wrong_answers))
    # Ask each question to the user
    for question, correct_answer, wrong_answers in questions:
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers)
        print(question)
        for i, answer in enumerate(answers):
            print(f'{i + 1}) {answer}') #This was fun to figure out how to do
        
        user_answer = input('Enter the number of the correct answer: ')
        
        if answers[int(user_answer) - 1] == correct_answer: # because lists start at zero not one
            score += 1
            print('\nCorrect!\n')
        else:
            print(f'Wrong! The correct answer was: {correct_answer}')
        
    print(f'\nYour final score is: {score}/{len(questions)}\n\n\n')
    if score == len(questions):
        print('Congratulations! You got all the questions right!')
    
main()