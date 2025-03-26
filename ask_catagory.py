import type
import os

def ask_catagory(questions_dict):
    os.system('cls||clear') # Clear the console for any system including stupid macs
    catagories = {category: questions for category, questions in questions_dict.items()} # This was fun to figure out, thanks stack overflow
    type.type("\u001b[32mPlease select a catagory:")
    print("\u001b[34m\u001b[0m", end="")

    for i, catagory_name in enumerate(catagories.keys(), 1): # Enumerate over the catagories and increment a number at the same time
        type.type(f'\u001b[33m{i}) \u001b[34m{catagory_name}')

    while True:   # Makes sure the input is valid
        user_input = type.typewriter_input('Enter the number of the catagory: ').strip()

        if user_input.isdigit() and  1 <= int(user_input) <= len(catagories): # input validation
            print("\u001b[34m\u001b[0m")
            break
        else:
            type.type('Invalid input. Please enter a number between 1 and ' + str(len(catagories)))
            print("\u001b[34m\u001b[0m", end="")

    selected_catagory = list(catagories.keys())[int(user_input) - 1] # Because the list index starts at 0 not 1
    return selected_catagory