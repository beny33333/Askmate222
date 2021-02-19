import csv
import os
"""Path to our data and define headers."""
ANSWER_FILE_PATH = os.getenv('ANSWER_FILE_PATH') if 'ANSWER_FILE_PATH' in os.environ else \
    'sample_data/answer.csv'
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_FILE_PATH = os.getenv('QUESTION_FILE_PATH') if 'QUESTION_FILE_PATH' in os.environ else \
    'sample_data/question.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image', 'active']

"""Import answers."""
def get_all_answers():
    answers = []
    with open(ANSWER_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
        for row in csv_reader:
            answers.append(row)
    return answers

"""Import questions."""
def get_all_questions():
    questions = []
    with open(QUESTION_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
        for row in csv_reader:
            questions.append(row)
    return questions


"""Generate the next id for the added question."""
def get_next_id():
    stories = get_all_questions()
    current_max = 0
    for story in stories:
        if int(story['id']) >= current_max:
            current_max = int(story['id'])

    return current_max + 1


"""Generate the next id for the added answer."""
def get_next_id_answer():
    stories = get_all_answers()
    current_max = 0
    for story in stories:
        if int(story['id']) >= current_max:
            current_max = int(story['id'])

    return current_max + 1


"""Taking all answers for the single question."""
def get_answers_for_the_question(single_id):
    answers = get_all_answers()
    answers_for_the_question = []
    for answer in answers:
        if int(single_id) == int(answer['question_id']):
            answers_for_the_question.append(answer)
    return answers_for_the_question


"""Taking question details."""
def get_one_question(single_id):
    questions = get_all_questions()
    single_question = []
    for question in questions:
        if int(single_id) == int(question['id']):
            zmienna = int(question['view_number'])
            zmienna += 1
            question['view_number'] = str(zmienna)
            single_question.append(question)
    save_user_story(questions, "w")
    return single_question


"""Export questions data."""
def save_user_story(question, mode):
    if mode == "a":
        with open(QUESTION_FILE_PATH, 'a', newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=QUESTION_HEADER, delimiter=';', quotechar='|')
            csv_writer.writerow(question)
    if mode == "w":
        with open(QUESTION_FILE_PATH, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(QUESTION_HEADER)
        with open(QUESTION_FILE_PATH, 'a', newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=QUESTION_HEADER, delimiter=';', quotechar='|')
            for element in question:
                csv_writer.writerow(element)


"""Export answers data."""
def save_user_answer(answer, mode):
    if mode == "a":
        with open(ANSWER_FILE_PATH, "a", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=ANSWER_HEADER, delimiter=';', quotechar='|')
            csv_writer.writerow(answer)
    if mode == "w":
        with open(ANSWER_FILE_PATH, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(ANSWER_HEADER)
        with open(ANSWER_FILE_PATH, 'a', newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=ANSWER_HEADER, delimiter=';', quotechar='|')
            for element in answer:
                csv_writer.writerow(element)


"""Deleting single question."""
def delete_question(question_id):
    questions = get_all_questions()
    for question in questions:
        if int(question['id']) == int(question_id):
            question['active'] += "frozen"
    return questions


"""Deleting single answer."""
def delete_answer(answer_id):
    answers = get_all_answers()
    for answer in answers:
        if int(answer['id']) == int(answer_id):
            answers.remove(answer)
    print(answers)
    return answers


"""Rating of the question."""
def votes(question_id, plus_or_minus):
    questions = get_all_questions()
    for question in questions:
        if int(question['id']) == int(question_id):
            if plus_or_minus == "+1":
                temp = int(question['vote_number'])
                temp += 1
                question['vote_number'] = str(temp)
            else:
                temp = int(question['vote_number'])
                temp -= 1
                question['vote_number'] = str(temp)
    return questions


"""Rating of the answer."""
def answer_votes(answer_id, plus_or_minus):
    answers = get_all_answers()
    for answer in answers:
        if int(answer['id']) == int(answer_id):
            if plus_or_minus == "+1":
                temp = int(answer['vote_number'])
                temp += 1
                answer['vote_number'] = str(temp)
            else:
                temp = int(answer['vote_number'])
                temp -= 1
                answer['vote_number'] = str(temp)
    print(answers)
    return answers


"""Handling actual id of displayed question in browser."""
def question_id_handler(question_id):
    f = open("sample_data/question_id_handler.txt", "w")
    f.write(str(question_id))
    f.close()


"""Taking actual id of displayed question in browser."""
def pull_question_id():
    f = open("sample_data/question_id_handler.txt", "r")
    question_id = f.read()
    return question_id
