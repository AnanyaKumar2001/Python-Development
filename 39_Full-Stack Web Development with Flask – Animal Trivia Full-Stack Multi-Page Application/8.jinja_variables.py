# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Jinja Variables


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html', message='Transmitting From The View Function')


if __name__ == "__main__":
    app.run(debug=True)
