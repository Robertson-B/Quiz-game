import json

def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions_dict = json.load(file)
    return questions_dict