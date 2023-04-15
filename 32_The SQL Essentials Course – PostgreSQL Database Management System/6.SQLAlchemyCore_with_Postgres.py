# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- SQLAlchemy Core Interactions with Postgres

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

engine = create_engine(
    "postgresql://m_helalee:12345678@localhost/company_sales")

with engine.connect() as connection:
    meta = MetaData(engine)

    sale_table = Table('sale', meta, autoload=True, autoload_with=engine)

    adding_record = sale_table.insert().values(order_num=1112135, order_type='Retail', cust_name="Muslim Helalee",
                                               prod_number="MH111", prod_name="HTML-CSS Bootcamp", quantity=15, price=10, discount=0, order_total=150)

    connection.execute(adding_record)

    # Reading
    select_statement = sale_table.select().limit(10)
    result_set = connection.execute(select_statement)
    for result in result_set:
        print("Reading:", result)

    # Updating
    update_statement = sale_table.update().where(
        sale_table.c.order_num == 1112135).values(quantity=2, order_total=20)
    connection.execute(update_statement)

    # Confirming Update
    reselect_statement = sale_table.select().where(sale_table.c.order_num == 1112135)
    updated_set = connection.execute(reselect_statement)
    for result in updated_set:
        print("Updated:", result)

    # Deleting
    delete_statement = sale_table.delete().where(sale_table.c.order_num == 1112135)
    connection.execute(delete_statement)

    # Confirming Delete
    not_found_set = connection.execute(reselect_statement)
    print("Deleted:", not_found_set.rowcount)
