# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Calling the Postgres Stored Procedure Using SQLAlchemy ORM


from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://m_helalee:12345678@localhost/company_sales')
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Sale(Base):
    __table__ = Base.metadata.tables['sale']

    def __repr__(self):
        return '''<Sale(order_num='{0}', order_type='{1}', cust_name='{2}',prod_name='{3}', quantity='{4}', order_total='{5})'>'''.format(self.order_num, self.order_type, self.cust_name, self.prod_name, self.order_total)


if __name__ == "__main__":
    with engine.connect() as connection:
        connection.execute("COMMIT")
        connection.execute(
            "CALL return_nondiscounted_item (%s, %s)", (1105910, 5))
