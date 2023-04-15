# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Running the Flask Development Server


from flask import Flask


app = Flask(__name__)


@app.route("/")
def welcome():
    return "This is my very first Flask application"


if __name__ == "__main__":
    app.run(debug=True)
