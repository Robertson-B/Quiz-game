import random
import ask_catagory

def ask_questions(questions_dict): # Asks the questions
    questions = questions_dict[ask_catagory.catagory]
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