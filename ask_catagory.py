def fetch_catagories(questions_dict):
    global catagories
    catagories = {category: questions for category, questions in questions_dict.items()}

def ask_catagory():
    global catagory
    print("Please select a catagory:")
    for i, catagory_name in enumerate(catagories.keys(), 1):
        print(f'{i}) {catagory_name}')
    while True:   # Makes sure the input is valid
        user_input = input('Enter the number of the catagory: ').strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(catagories):
            print("")
            break
        else:
            print('Invalid input. Please enter a number between 1 and', len(catagories))
    catagory = list(catagories.keys())[int(user_input) - 1]