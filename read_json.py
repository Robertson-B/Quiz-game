import json
# Reads the json file and converts it into a massive dictionary
# This is simplier and more efficient than scanning the JSON file every time we need to access a question or answer
def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions_dict = json.load(file)
    return questions_dict
# Thanks stack overflow for the eligent solution. Mine was a 50 line nighmare