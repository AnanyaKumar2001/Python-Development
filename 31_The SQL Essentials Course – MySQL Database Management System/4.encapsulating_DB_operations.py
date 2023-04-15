# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Encapsulating Database Operations

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


def add_new_topic(cursor, topic_title, topic_category, task_descriptions):
    topic_data = (topic_title, topic_category)

    cursor.execute("""INSERT INTO topics(title, category)
                                VALUES(%s, %s)
                                 """, topic_data)

    topic_id = cursor.lastrowid

    tasks_data = []

    for description in task_descriptions:
        task_data = (topic_id, description)
        tasks_data.append(task_data)

    cursor.executemany('''INSERT INTO tasks(topic_id, description) 
                                          VALUES(%s, %s)
                                          ''', tasks_data)


if __name__ == "__main__":
    db = connect("blogs")

    cursor = db.cursor()

    # adding new records
    # tasks = ['clear the browser cache', "use a different browser"]

    # add_new_topic(cursor, "Gmail not opening", "Social", tasks)
    # db.commit()

    cursor.execute("SELECT * FROM topics")
    topic_records = cursor.fetchall()
    print(topic_records)

    cursor.execute("SELECT * FROM tasks")
    task_records = cursor.fetchall()
    print(task_records)

    db.close()
