# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Debugging


from flask import Flask


app = Flask(__name__)


@app.route("/")
def welcome():
    return "This is my very first Flask application"


@app.route('/cool')
def cool():
    return "Flask is AWESOME!!!"


counter = 0


@app.route('/view_count')
def view_count():
    global counter
    counter += 1
    return f"This is page has been viewed {counter} time(s)"


if __name__ == "__main__":
    app.run(debug=True)
