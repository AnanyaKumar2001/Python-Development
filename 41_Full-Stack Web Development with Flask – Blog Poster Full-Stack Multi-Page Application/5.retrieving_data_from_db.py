# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Retrieving Data From The Database & Inserting it into Our Flask App

from logging import debug
from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/blog_poster'

app.config['SECRET_KEY'] = '\xff\x98Tq\x80\xf3\xb6\xac=\x10\xbfG\x9a\x98\x1e\xab098fi\xed\x1d@'

db = SQLAlchemy(app)


class Topic(db.Model):
    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255))


class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.topic_id'))
    description = db.Column(db.String(length=255))

    topic = db.relationship("Topic")


@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", topic=Topic.query.filter_by(topic_id=topic_id).first(), tasks=Task.query.filter_by(topic_id=topic_id).all())


@app.route('/add/topic', methods=["POST"])
def add_topic():
    # add topic functionality

    return "Topic Added Successfully"


@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    # add task functionality

    return "Task Added Successfully"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5533)
