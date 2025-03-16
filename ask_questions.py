import random
import ask_catagory
import type
import threading
import time

output_lock = threading.Lock()
max_score = 0

def ask_questions(questions_dict, player_name): # Asks the questions
    questions = questions_dict[ask_catagory.catagory]
    random.shuffle(questions)
    score = 0
    global max_score
    max_score = 0

    def timer():
        global time_up
        global max_score
        time_up = True
        with output_lock:
            max_score += 1
            type.type("\n\nTime's up! Press enter to continue.")
            print("\u001b[34m\u001b[0m", end="")
            type.type("\u001b[32mThe correct answer was: " + str(correct_answer) + "")
            type.type("\u001b[32mYour score is: " + str(score) + "/" + str(max_score) + "\n")

    for i in questions:
        global time_up
        question = i['question']
        correct_answer = i['correct_answer']
        wrong_answers = i['wrong_answers']
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
                max_score += 1
                type.type('\n\u001b[32mCorrect!')
                type.type("Your score is: " + str(score) + "/" + str(max_score) + "\n")
            elif not time_up:
                max_score += 1
                type.type('\n\u001b[31;1mWrong! The correct answer was: ' + str(correct_answer))
                print("\u001b[34m\u001b[0m", end="")
                type.type("\u001b[32mYour score is: " + str(score) + "/" + str(max_score) + "\n")

    with output_lock:
        if score == len(questions): # Print user score
            type.type('Your final score is: ' + str(score) + "/" + str(len(questions)))
            type.type(f'Congratulations {player_name}! You got all the questions right!\n\n\n\n')
            time.sleep(2)
        else:
            type.type('\nYour final score is: ' + str(score) + "/" + str(len(questions)))
            type.type(f'Better luck next time {player_name}!\n\n\n\n')
            time.sleep(2)