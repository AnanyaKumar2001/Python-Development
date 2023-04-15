# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Connecting a Python App to the MySQL Database

import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(
            host="localhost",
            user="root",
            password="!23QweAsdZxc",
            database=db_name
        )

    except Error as err:
        print(err)


if __name__ == "__main__":
    db = connect("blogs")

    cursor = db.cursor()

    cursor.execute("SELECT * FROM topics")
    topic_records = cursor.fetchall()
    print(topic_records)

    cursor.execute("SELECT * FROM tasks")
    task_records = cursor.fetchall()
    print(task_records)

    db.close()
