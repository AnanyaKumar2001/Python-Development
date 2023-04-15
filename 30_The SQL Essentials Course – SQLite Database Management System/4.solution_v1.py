import sqlite3

with sqlite3.connect("students_sqlite.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Students 
                    (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    email_address TEXT
                     )""")

    # student_records = [
    #     ("Alexander", "Hunold", "alexander.hunold@el.cool"),
    #     ("Nancy", "Pelosi", "nancy.pelosi@el.cool"),
    #     ("Irene", "Mikkilineni", "irene.mikkilineni@el.cool"),
    #     ("Sarah", "Bell", "sarah.bell@el.cool")
    # ]

    # cursor.executemany('''INSERT INTO Students (first_name, last_name, email_address)
    #                       VALUES (?,?,?) ''', student_records)

    # cursor.execute("SELECT * FROM Students")
    # print(cursor.fetchall())

    cursor.execute("SELECT email_address FROM Students")
    print(cursor.fetchall())

    connection.commit()
