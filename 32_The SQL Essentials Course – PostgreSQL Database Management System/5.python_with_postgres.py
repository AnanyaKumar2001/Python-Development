# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Python Interactions with a Postgres Database


import psycopg2


def insert_sale(connection, order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount

    sale_data = (order_num, order_type, cust_name, prod_number,
                 prod_name, quantity, price, discount, order_total)

    cursor = connection.cursor()

    cursor.execute("""INSERT INTO sale (ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT,    ORDER_TOTAL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """, sale_data)

    connection.commit()

    cursor.execute(
        "SELECT CUST_NAME, ORDER_TOTAL FROM sale WHERE ORDER_NUM=%s", (order_num, ))

    rows = cursor.fetchall()

    for row in rows:
        print("Customer Name:", row[0])
        print("Total Order:", row[1])


if __name__ == "__main__":
    connection = psycopg2.connect(
        database="company_sales", user="m_helalee", password="12345678", host="localhost", port="5432")

    order_num = int(input("What is the order number?\n"))
    order_type = input("What is the order type (Retail/Wholesale)?\n")
    cust_name = input("What is the customer's name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = float(input("How many were bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))

    insert_sale(connection, order_num, order_type, cust_name,
                prod_number, prod_name, quantity, price, discount)

    connection.close()
