import csv
import os

ANSWER_FILE_PATH = os.getenv('ANSWER_FILE_PATH') if 'ANSWER_FILE_PATH' in os.environ else \
    'C:/Users/macie/PycharmProjects/ask-mate-1-python-maciejlewicki95/sample_data/answer.csv'
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_FILE_PATH = os.getenv('QUESTION_FILE_PATH') if 'QUESTION_FILE_PATH' in os.environ else\
    'C:/Users/macie/PycharmProjects/ask-mate-1-python-maciejlewicki95/sample_data/question.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


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


def save_user_story(question):
    with open(QUESTION_FILE_PATH, 'a', newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=QUESTION_HEADER, delimiter=';', quotechar='|')
        csv_writer.writerow(question)


def save_user_answer(answer):
    with open(ANSWER_FILE_PATH, 'a', newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=ANSWER_HEADER, delimiter=';', quotechar='|')
        csv_writer.writerow(answer)