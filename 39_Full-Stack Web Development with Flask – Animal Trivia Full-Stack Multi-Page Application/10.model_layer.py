# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- The Model Layer


from flask import Flask, render_template
from model import db


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html',
                           message='Transmitting From The View Function',
                           first_name="Muslim",
                           last_name="Helalee")


@app.route('/questions')
def questions_view():
    questions_db = db[0]
    return render_template('quiz.html', question=questions_db)


if __name__ == "__main__":
    app.run(debug=True)
