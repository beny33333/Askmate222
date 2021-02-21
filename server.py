from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    list_of_questions = data_handler.get_all_questions()
    questions = []
    for question in list_of_questions:
        if question['active'] != "frozen":
            questions.append(question)
    headers = data_handler.QUESTION_HEADER
    return render_template('list.html', questions=questions, headers=headers)


@app.route('/add-question')
def display_add_question():
    return render_template('add.html')


@app.route('/add-question', methods=['POST'])
def add_question():
    question = dict(request.form)
    question['id'] = data_handler.get_next_id()
    question['vote_number'] = "0"
    question['view_number'] = "0"
    data_handler.save_user_story(question, "a")
    return redirect(url_for('route_list'))


@app.route('/question/<int:user>')
def display_one_question(user):
    question = data_handler.get_one_question(user)
    answers = data_handler.get_answers_for_the_question(user)
    length = len(answers)
    question_id = user
    data_handler.question_id_handler(question_id)
    return render_template('one_question.html', question=question, answers=answers, question_id=question_id, length=length)


@app.route('/question/<int:user>/new-answer')
def display_add_answer(user):
    question_id = user
    return render_template('add_answer.html', question_id=question_id)


@app.route('/question/<int:user>/new-answer', methods=['POST'])
def add_new_answer(user):
    answer = dict(request.form)
    answer['id'] = data_handler.get_next_id_answer()
    answer['question_id'] = int(user)
    answer['vote_number'] = "0"
    data_handler.save_user_answer(answer, 'a')
    return redirect(url_for('display_one_question', user=user))


@app.route('/question/<int:user>/delete')
def delete_question(user):
    questions = data_handler.delete_question(user)
    data_handler.save_user_story(questions, "w")
    return redirect(url_for('route_list'))


@app.route('/question/<int:user>/vote_up')
def vote_up(user):
    questions = data_handler.votes(user, "+1")
    data_handler.save_user_story(questions, "w")
    return redirect(url_for('route_list'))


@app.route('/question/<int:user>/vote_down')
def vote_down(user):
    questions = data_handler.votes(user, "-1")
    data_handler.save_user_story(questions, "w")
    return redirect(url_for('route_list'))


@app.route('/answer/<int:answer_id>/vote_up/')
def vote_up_answer(answer_id):
    answers = data_handler.answer_votes(answer_id, "+1")
    data_handler.save_user_answer(answers, 'w')
    user = data_handler.pull_question_id()
    return redirect(url_for('display_one_question', user=user))


@app.route('/answer/<int:answer_id>/vote_down')
def vote_down_answer(answer_id):
    answers = data_handler.answer_votes(answer_id, "-1")
    data_handler.save_user_answer(answers, 'w')
    user = data_handler.pull_question_id()
    return redirect(url_for('display_one_question', user=user))


@app.route('/answer/<int:answer_id>/delete')
def delete_answer(answer_id):
    answers = data_handler.delete_answer(answer_id)
    data_handler.save_user_answer(answers, 'w')
    user = data_handler.pull_question_id()
    return redirect(url_for('display_one_question', user=user))


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )
