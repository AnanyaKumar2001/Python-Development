# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Creating a Flask App

from logging import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_topics():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5533)
