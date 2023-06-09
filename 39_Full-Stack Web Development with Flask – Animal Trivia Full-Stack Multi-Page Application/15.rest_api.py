# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Creating a REST API in Flask


from flask import Flask, render_template, abort, jsonify
from model import db


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html',
                           questions=db)


@app.route('/questions/<int:index>')
def questions_view(index):

    try:
        questions_db = db[index]
        return render_template('quiz.html',
                               question=questions_db,
                               index=index,
                               max_index=len(db) - 1)

    except IndexError:
        abort(404)


# Creating a REST API for our Full-Stack Multi-Page App
@app.route('/api/question/')
def api_question_list():
    return jsonify(db)


@app.route('/api/question/<int:index>')
def api_question_detail(index):
    try:
        return db[index]

    except IndexError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
