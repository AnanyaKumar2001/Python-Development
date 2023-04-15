# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Calling the Postgres Stored Procedure Using SQLAlchemy Core


from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine(
    "postgresql://m_helalee:12345678@localhost/company_sales")

with engine.connect() as connection:
    meta = MetaData(engine)

    sales_table = Table('sale', meta, autoload=True, autoload_with=engine)

    connection.execute("COMMIT")
    connection.execute("CALL return_nondiscounted_item (%s, %s)", (1105910, 2))
