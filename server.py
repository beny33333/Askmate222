from flask import Flask, render_template

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    questions = data_handler.get_all_questions()
    headers = data_handler.get_headers()

    return render_template('list.html', questions=questions, headers=headers)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )
