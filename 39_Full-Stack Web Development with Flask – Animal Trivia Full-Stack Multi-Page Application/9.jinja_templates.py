# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Jinja Templates


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html',
                           message='Transmitting From The View Function',
                           first_name="Muslim",
                           last_name="Helalee")


if __name__ == "__main__":
    app.run(debug=True)
