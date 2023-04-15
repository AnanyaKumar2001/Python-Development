# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- How Flask Maps URLs to View Functions

from flask import Flask


app = Flask(__name__)


# the first page
@app.route("/")
def welcome():
    return "This is my very first Flask application"


# the second page
@app.route("/cool")
def cool():
    return "Flask is AWESOME!!!"


counter = 0


# third page
@app.route("/view_count")
def view_count():
    global counter
    counter += 1
    return f"This page has been viewed {counter} time(s)"


if __name__ == "__main__":
    app.run(debug=True)
