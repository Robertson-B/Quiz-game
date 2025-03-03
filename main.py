import csv
import random

file_path = 'questions.csv'
questions = []

# Read questions from the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        question = row[0]
        correct_answer = row[1]
        wrong_answers = row[2:]
        questions.append((question, correct_answer, wrong_answers))

score = 0

# Ask each question to the user
for question, correct_answer, wrong_answers in questions:
    answers = wrong_answers + [correct_answer]
    random.shuffle(answers)
    
    print(question)
    for i, answer in enumerate(answers):
        print(f'{i + 1}) {answer}')
    
    user_answer = input('Enter the number of the correct answer: ')
    
    if answers[int(user_answer) - 1] == correct_answer:
        score += 1
        print('Correct!')
    else:
        print(f'Wrong! The correct answer was: {correct_answer}')
    
print(f'Your final score is: {score}/{len(questions)}')