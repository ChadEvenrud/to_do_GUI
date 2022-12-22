import requests
import random

data_request = requests.get("https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple")

data_file = data_request.json()

for data in data_file["results"]:
    question = data["question"]
    correct_answer = data["correct_answer"]
    wrong_answers = data["incorrect_answers"]
    
    for index, option in enumerate(wrong_answers):
        print(index,option)
                