# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Inserting Data into Our Database From a CSV File


import psycopg2

connection = psycopg2.connect(
    database="company_sales",
    user="m_helalee",
    password="12345678",
    host="localhost",
    port="5432"
)


cursor = connection.cursor()

# cursor.execute("SELECT * FROM sale LIMIT 10")
# print(cursor.fetchall())


cursor.execute("INSERT INTO sale (ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES (1105910, 'Retail', 'Evolutive Learning', 'PY999', 'Complete Python Bootcamp', 3, 19, 0, 57)")

connection.commit()

cursor.execute(
    "SELECT CUST_NAME, PROD_NAME, ORDER_TOTAL FROM sale WHERE ORDER_NUM=1105910")

rows = cursor.fetchall()

for row in rows:
    print("Customer Name:", row[0])
    print("Product Name:", row[1])
    print("Order Total:", row[2])


connection.close()
