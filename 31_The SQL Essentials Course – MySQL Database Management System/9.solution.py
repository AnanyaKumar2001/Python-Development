# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Creating a MySQL Database


import pandas
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# connect to the engine
engine = create_engine(
    'mysql+mysqlconnector://root:!23QweAsdZxc@localhost:3306/company_sales')

Base = declarative_base()


class Sale(Base):
    __tablename__ = 'sales'
    __tableargs__ = {"schema": "company_sales"}

    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(250))
    cust_name = Column(String(250))
    prod_number = Column(String(250))
    prod_name = Column(String(250))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    # we only the most important columns
    def __repr__(self):
        return "< Sale(order_num='{0}', order_type='{1}', cust_name='{2}', prod_name='{3}', quantity='{4}', order_total='{5}'>".format(self.order_num, self.order_type, self.cust_name, self.prod_name, self.quantity, self.order_total)


Base.metadata.create_all(engine)

file_name = "company_sales.csv"
data_frame = pandas.read_csv(file_name)
data_frame.to_sql(con=engine, name=Sale.__tablename__,
                  if_exists='replace', index=False)


session = sessionmaker()
session.configure(bind=engine)
s = session()

overall_max = s.query(func.max(Sale.order_total)).scalar()
print("The biggest order:", overall_max)

results = s.query(Sale).order_by(Sale.order_total.desc()).limit(10)

for result in results:
    print(result)
