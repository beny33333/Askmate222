import csv
import os

QUESTION_FILE_PATH = os.getenv('QUESTION_FILE_PATH') if 'QUESTION_FILE_PATH' in os.environ else 'sample_data/question.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def get_all_questions():
    questions = []
    with open(QUESTION_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='|')
        for row in csv_reader:
            questions.append(row)
    return questions
