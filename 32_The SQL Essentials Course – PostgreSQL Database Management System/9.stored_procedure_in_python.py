# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Calling the Postgres Stored Procedure in Python

import psycopg2

if __name__ == "__main__":
    connection = psycopg2.connect(database="company_sales",
                                  user="m_helalee",
                                  password="12345678",
                                  host="localhost",
                                  port="5432")

    connection.autocommit = True

    cursor = connection.cursor()

    cursor.execute('''CALL return_nondiscounted_item(%s, %s)''', (1105910, 1))

    connection.close()
