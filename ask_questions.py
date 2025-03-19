import random
import ask_catagory
import type
import threading
import time
import music

def ask_questions(questions_dict, player_name):
    #Asks the questions from the quiz.
    output_lock = threading.Lock()
    questions = questions_dict[ask_catagory.catagory]
    random.shuffle(questions)
    score = 0
    state = {'max_score': 0, 'time_up': False}

    def timer(correct_answer, score):
        #Handles the timer expiration.
        state['time_up'] = True
        with output_lock:
            state['max_score'] += 1
            print("\n\nTime's up! Press enter to continue.")
            print("\u001b[34m\u001b[0m", end="")
            print("\u001b[32mThe correct answer was: " + str(correct_answer))
            print("\u001b[32mYour score is: " + str(score) + "/" + str(state['max_score']) + "\n")

    for i in questions:
        question = i['question']
        correct_answer = i['correct_answer']
        wrong_answers = i['wrong_answers']
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers)

        with output_lock:
            type.type("\u001b[32m" + question)
            for idx, answer in enumerate(answers):
                type.type(f'\u001b[33m{idx + 1}) \u001b[34m{answer}')

        state['time_up'] = False
        timer_thread = threading.Timer(32, timer, args=(correct_answer, score))
        music.quiz_theme()
        timer_thread.start()

        while True:
            user_answer = type.typewriter_input('Enter the number of the correct answer: ').strip()
            if state['time_up']:
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                break
            elif user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                timer_thread.cancel()
                music.stop_music()
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                break
            else:
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                    if not state['time_up']:
                        type.type('\u001b[31;1mInvalid input. Please enter a number between 1 and ' + str(len(answers)))
                        print("\u001b[34m\u001b[0m", end="")

        with output_lock:
            if not state['time_up'] and answers[int(user_answer) - 1] == correct_answer:
                score += 1
                state['max_score'] += 1
                music.correct_answer()
                type.type('\n\u001b[32mCorrect!')
                type.type("Your score is: " + str(score) + "/" + str(state['max_score']) + "\n")
            elif not state['time_up']:
                state['max_score'] += 1
                music.wrong_answer()
                type.type('\n\u001b[31;1mWrong! The correct answer was: ' + str(correct_answer))
                print("\u001b[34m\u001b[0m", end="")
                type.type("\u001b[32mYour score is: " + str(score) + "/" + str(state['max_score']) + "\n")

    with output_lock:
        if score == len(questions):
            type.type('Your final score is: ' + str(score) + "/" + str(len(questions)))
            type.type(f'Congratulations {player_name}! You got all the questions right!\n\n\n\n')
        else:
            type.type('\nYour final score is: ' + str(score) + "/" + str(len(questions)))
            type.type(f'Better luck next time {player_name}!\n\n\n\n')
        time.sleep(2)