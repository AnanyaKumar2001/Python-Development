# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Adding Data

import sqlite3

with sqlite3.connect("movie_library.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''
                  CREATE TABLE IF NOT EXISTS Movies (
                    Title TEXT,
                    Director TEXT,
                    Year INT
                  )
                 ''')
    # adding records
    # cursor.execute(
    #     "INSERT INTO Movies VALUES ('Avatar', 'James Cameron', 2009)")

    # fetching records
    # cursor.execute("SELECT * FROM Movies")
    # print(cursor.fetchone())

    # adding more records
    # high_earning_movies = [
    #     ("Avengers: Endgame", "Russo Brothers", 2019),
    #     ("Star Wars: The Force Awakens", "J. J. Abrams", 2015),
    #     ("The Avengers", "Joss Whedon", 2012),
    #     ("Froaen", "Chris Buck", 2013)
    # ]

    # cursor.executemany("INSERT INTO Movies VALUES (?,?,?)",
    #                    high_earning_movies)

    records = cursor.execute("SELECT * FROM Movies")
    # print(cursor.fetchall())

    for record in records:
        print(record)

    # Filter records
    # release_year = (2015,)
    # cursor.execute("SELECT * FROM Movies WHERE Year>=?", release_year)

    # print(cursor.fetchall())

    connection.commit()
