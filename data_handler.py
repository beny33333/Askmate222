import csv
import os
import util

ANSWER_FILE_PATH = os.getenv('ANSWER_FILE_PATH') if 'ANSWER_FILE_PATH' in os.environ else \
    'sample_data/answer.csv'
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_FILE_PATH = os.getenv('QUESTION_FILE_PATH') if 'QUESTION_FILE_PATH' in os.environ else\
    'sample_data/question.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image', 'active']
# SUBMISSION_TIME_INDEX = 1


def get_all_answers():
    answers = []
    with open(ANSWER_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
        for row in csv_reader:
            answers.append(row)
    return answers


def get_all_questions():
    questions = []
    with open(QUESTION_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
        for row in csv_reader:
            questions.append(row)
            # questions.append(util.conver_UNIX_to_datetime(row, 'submission_time'))
    return questions


def get_next_id():
    stories = get_all_questions()
    current_max = 0
    for story in stories:
        if int(story['id']) >= current_max:
            current_max = int(story['id'])

    return current_max + 1


def get_answers_for_the_question(single_id):
    answers = get_all_answers()
    answers_for_the_question = []
    for answer in answers:
        if int(single_id) == int(answer['question_id']):
            answers_for_the_question.append(answer)
    return answers_for_the_question


def get_one_question(single_id):
    questions = get_all_questions()
    single_question = []
    for question in questions:
        if int(single_id) == int(question['id']):
            single_question.append(question)
    return single_question


def get_next_id_answer():
    stories = get_all_answers()
    current_max = 0
    for story in stories:
        if int(story['id']) >= current_max:
            current_max = int(story['id'])

    return current_max + 1


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


def save_user_answer(answer):
    with open(ANSWER_FILE_PATH, "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=ANSWER_HEADER, delimiter=';', quotechar='|')
        csv_writer.writerow(answer)


def delete_question(question_id):
    questions = get_all_questions()
    for question in questions:
        if int(question['id']) == int(question_id):
            question['active'] += "frozen"
    return questions


def votes(question_id, plus_or_minus):
    questions = get_all_questions()
    for question in questions:
        if int(question['id']) == int(question_id):
            if plus_or_minus == "+1":
                zmienna = int(question['vote_number'])
                zmienna += 1
                question['vote_number'] = str(zmienna)
            else:
                zmienna = int(question['vote_number'])
                zmienna -= 1
                question['vote_number'] = str(zmienna)
    print(questions)
    return questions
