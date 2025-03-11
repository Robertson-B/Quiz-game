import type

def ask_catagory(questions_dict):
    global catagories
    catagories = {category: questions for category, questions in questions_dict.items()}
    global catagory
    type.type("Please select a catagory:")
    for i, catagory_name in enumerate(catagories.keys(), 1):
        type.type(f'{i}) {catagory_name}')
    while True:   # Makes sure the input is valid
        user_input = type.typewriter_input('Enter the number of the catagory: ').strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(catagories):
            print("\u001b[34m\u001b[0m")
            break
        else:
            type.type('Invalid input. Please enter a number between 1 and', len(catagories))
    catagory = list(catagories.keys())[int(user_input) - 1]