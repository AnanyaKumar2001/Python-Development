# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Flask App Flow Control


from flask import Flask


app = Flask(__name__)


@app.route("/")
def welcome():
    return "This is my very first Flask application"


@app.route('/cool')
def cool():
    return "Flask is AWESOME!!!"


if __name__ == "__main__":
    app.run(debug=True)
