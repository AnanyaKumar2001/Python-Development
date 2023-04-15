# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Using MySQL to Import CSV Data


import mysql.connector as mysql
import csv

connection = mysql.connect(
    user="root",
    password="!23QweAsdZxc",
    host="localhost",
    database="sales",
    allow_local_infile=True
)

cursor = connection.cursor()

query = ''' CREATE TABLE salespeople (
  id INT(255) NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email_address VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
)'''

cursor.execute("DROP TABLE IF EXISTS salespeople")

cursor.execute(query)

# Method one ->>>>> inserting data into DB from CSV
# with open("salespeople.csv", 'r') as file:
#     csv_data = csv.reader(file)

#     for row in csv_data:
#         print("Row is a list:", row)

#         row_tuple = tuple(row)
#         cursor.execute("""INSERT INTO salespeople (first_name, last_name, email_address, city, state)
#                                   VALUES("%s", "%s", "%s", "%s", "%s")
#                                    """, row_tuple)


# Method two ->>>>> using a specific SQL command to insert data
q = """LOAD DATA LOCAL INFILE 'C:/salespeople.csv' INTO TABLE salespeople FIELDS TERMINATED BY ',' ENCLOSED BY '"' (first_name, last_name, email_address, city, state);"""

cursor.execute(q)

connection.commit()

cursor.execute("SELECT * FROM salespeople LIMIT 10")
print(cursor.fetchall())

connection.close()

# You might get this error
# LOAD DATA LOCAL INFILE file request rejected due to restrictions on access

# if you get this error
"""
1- Open command line in MySQL

2- type ->>>>> show global variables like 'local_infile';

3- type ->>>>> set global local_infile=true;
"""
