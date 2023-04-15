# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- SQLAlchemy ORM Interactions with Postgres

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
        return '''<Sale(order_num='{0}', order_type'{1}', cust_name='{2}', 
            prod_name='{3}', quantity='{4}', 
            order_total='{5}')>'''.format(self.order_num,
                                          self.order_type, self.cust_name, self.prod_name,
                                          self.quantity, self.order_total)


def load_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = load_session()

    # Read
    smallest_sales = session.query(Sale).order_by(Sale.order_total).limit(10)
    print("Smallest:", smallest_sales[0].cust_name)

    # Insert
    # insert_sale = Sale(order_num=1009988, order_type='Retail', cust_name='Udemy', prod_number='AI999',
    #                    prod_name='Understanding Artificial Intelligence', quantity=5, price=75, discount=0, order_total=375)
    # print("New Record:", insert_sale)

    # session.add(insert_sale)
    # session.commit()

    # Update
    # insert_sale.quantity = 4
    # insert_sale.order_total = 300
    # session.commit()

    # updated_sale = session.query(Sale).filter(
    #     Sale.order_num == 1009988).first()
    # print("Updated Record:", updated_sale)

    # Delete
    returned_sale = session.query(Sale).filter(
        Sale.order_num == 1009988).first()

    session.delete(returned_sale)
    session.commit()
