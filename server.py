from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_handler.get_all_questions()
    headers = data_handler.QUESTION_HEADER

    return render_template('list.html', questions=questions, headers=headers)


@app.route('/add-question')
def display_add_question():
    return render_template('add.html')


@app.route('/add-question', methods=['POST'])
def add_question():
    question = dict(request.form)
    question['id'] = data_handler.get_next_id()
    data_handler.save_user_story(question)
    print(question)
    return redirect(url_for('route_list'))


@app.route('/question/<int:user>')
def display_one_question(user):
    question = data_handler.get_one_question(user)
    answers = data_handler.get_answers_for_the_question(user)
    return render_template('one_question.html', question=question, answers=answers)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )
