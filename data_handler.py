import csv
import os

QUESTION_FILE_PATH = os.getenv('QUESTION_FILE_PATH') if 'QUESTION_FILE_PATH' in os.environ else\
    'C:/Users/macie/PycharmProjects/ask-mate-1-python-maciejlewicki95/sample_data/question.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


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


def get_one_question(single_id):
    questions = get_all_questions()
    single_question = []
    for question in questions:
        if int(single_id) == int(question['id']):
            single_question.append(question)
    return single_question


def save_user_story(question):
    with open(QUESTION_FILE_PATH, 'a', newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=QUESTION_HEADER, delimiter=';', quotechar='|')
        csv_writer.writerow(question)
