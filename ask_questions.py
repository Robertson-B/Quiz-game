import random
import ask_catagory
import type
import threading

output_lock = threading.Lock()

def ask_questions(questions_dict): # Asks the questions
    questions = questions_dict[ask_catagory.catagory]
    random.shuffle(questions)
    score = 0

    def timer():
        global time_up
        time_up = True
        with output_lock:
            type.type("\n\nTime's up! Press enter to continue.")

    for question_data in questions:
        global time_up
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        wrong_answers = question_data['wrong_answers']
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers)
        with output_lock:
            type.type("\u001b[32m" + question)
            for i, answer in enumerate(answers):
                type.type(f'\u001b[33m{i + 1}) \u001b[34m{answer}') # This was fun to figure out how to do

        time_up = False
        timer_thread = threading.Timer(20.0, timer)
        timer_thread.start()

        while True: # Makes sure the input is valid
            user_answer = type.typewriter_input('Enter the number of the correct answer: ').strip()
            if time_up:
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                break
            elif user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                timer_thread.cancel()
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                break
            else:
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                    if not time_up:
                        type.type('\u001b[31;1mInvalid input. Please enter a number between 1 and ' + str(len(answers)))
                        print("\u001b[34m\u001b[0m", end="")

        with output_lock:
            if not time_up and answers[int(user_answer) - 1] == correct_answer: # Because lists start at zero not one
                score += 1
                type.type('\n\u001b[32mCorrect!\n')
            elif not time_up:
                type.type('\n\u001b[31;1mWrong! The correct answer was: ' + str(correct_answer) + "\n")
                print("\u001b[34m\u001b[0m", end="")

    with output_lock:
        if score == len(questions): # Print user score
            type.type('\nYour final score is: ' + str(score) + "/" + str(len(questions)))
            type.type('Congratulations! You got all the questions right!\n\n\n')
        else:
            type.type('\nYour final score is: ' + str(score) + "/" + str(len(questions)))
            type.type('Better luck next time!\n\n\n')