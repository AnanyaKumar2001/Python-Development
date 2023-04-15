# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Create a Postgres Database


""" Tasks
1- Create a library DB to store authors and their books
2- The DB will have 3 table; authors, books, authorbooks
3- The Authors table will have the following columns; id, first name & last name
4- The Books table will have the following columns; id, title & number of pages
5- The AuthorBooks table will have the following columns; id, author id & book id

-- Separating the author books allows us to easily store multiple books by the same author. 
-- For books with multiple authors, multiple entries would be added to the authorbooks table

-- Once the database is created with the necessary tables, you will add functionality to add a new book to the DB. The following operations must be added.

6- The books table should be updated with the new book
7- if author is a new author, then authors table should be updated to include the new author, if the author is not a new author, then the author will not be added to the authors table again
8- You will also add a new pairing to the authorbooks table
9- all these operations must be done within a transaction, so the DB will never end up in a half done state. for this you can use stored procedures or transactions

---------------------------------------------------
You can use psycopg2 module, SQLAlchemy Core or SQLAlchemy ORM.
My Solution will focus on SQLAlchemy ORM
"""
