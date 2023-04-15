# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Creating Our First Flask Application

# 1- Jinja
# 2- Werkzeug

# installing flask
# *-*-*-* pipenv install flask

from flask import Flask


app = Flask(__name__)


@app.route('/')
def welcome():
    return 'This is my very first flask app'


if __name__ == '__main__':
    app.run(debug=True)
