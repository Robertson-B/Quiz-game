import random
import type
import threading
import time
import music
import leaderboard

def ask_questions(questions_dict, player_name, selected_category):
    # Asks the questions
    output_lock = threading.Lock() # Output lock to prevent multiple threads from writing to the console at the same time
    questions = questions_dict[selected_category]
    random.shuffle(questions)
    score = 0
    max_score = 0
    time_up = False

    def timer(correct_answer, score, max_score): # A "very simple" timer function for questions.
        # Timer for questions
        nonlocal time_up # Technically not a global varible
        time_up = True
        with output_lock:
            max_score += 1
            print("\n\nTime's up! Press enter to continue.")
            print("\u001b[34m\u001b[0m", end="")
            print("\u001b[32mThe correct answer was: " + str(correct_answer))
            print("\u001b[32mYour score is: " + str(score) + "/" + str(max_score) + "\n")
            max_score += 1

    for question_data in questions: # question data is just a replacement for i 
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        wrong_answers = question_data['wrong_answers']
        answers = wrong_answers + [correct_answer]
        random.shuffle(answers)

        with output_lock:
            type.type("\u001b[32m" + question)
            for i, answer in enumerate(answers): # Enumerate is a function that returns the index and the value of the list simulataneously
                type.type(f'\u001b[33m{i + 1}) \u001b[34m{answer}')

        time_up = False
        timer_thread = threading.Timer(32, timer, args=(correct_answer, score, max_score)) # Have to do it this way or things break, not sure why
        music.quiz_theme() # jepordy theme
        timer_thread.start()

        while True:
            user_answer = type.typewriter_input('Enter the number of the correct answer: ').strip()

            if time_up:
                with output_lock:
                    print("\u001b[34m\u001b[0m", end="")
                break
            elif user_answer.isdigit() and 1 <= int(user_answer) <= len(answers): # Modular input validation
                timer_thread.cancel()
                music.stop_music()
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
            if not time_up and answers[int(user_answer) - 1] == correct_answer:
                score += 1
                max_score += 1
                music.correct_answer()
                type.type('\n\u001b[32mCorrect!')
                type.type("Your score is: " + str(score) + "/" + str(max_score) + "\n")
            elif not time_up:
                max_score += 1
                music.wrong_answer()
                type.type('\n\u001b[31;1mWrong! The correct answer was: ' + str(correct_answer))
                print("\u001b[34m\u001b[0m", end="")
                type.type("\u001b[32mYour score is: " + str(score) + "/" + str(max_score) + "\n")

    with output_lock:
        leaderboard.update_leaderboard(player_name, score, selected_category, max_score) # Stores score to a leaderboard csv file
        time.sleep(2)