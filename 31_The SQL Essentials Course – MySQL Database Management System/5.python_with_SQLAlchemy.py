# *-*-*-*-*-*-*-*-* ---- ----------------------- ---- *-*-*-*-*-*-*-*-*
# *-*-*-*-*-*-*-*-* ---- Connecting Our Python App + SQLAlchemy ORM to a Database

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+mysqlconnector://root:!23QweAsdZxc@localhost:3306/to_do_list", echo=True)

Base = declarative_base()


class Topic(Base):
    # table attribute
    __tablename__ = "topics"
    __table_args__ = {"schema": "to_do_list"}

    # setting up the columns
    topic_id = Column(Integer, primary_key=True)
    title = Column(String(length=100))
    description = Column(String(length=255))

    def __repr__(self):
        return "<Topic(title'{0}', description='{1})'>".format(self.title, self.description)


class Task(Base):
    # table attribute
    __tablename__ = "tasks"
    __table_args__ = {"schema": "to_do_list"}

    # setting up the columns
    task_id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('to_do_list.topics.topic_id'))
    description = Column(String(length=255))

    # building the relationship
    topic = relationship("Topic")

    def __repr__(self):
        return "<Task(description='{0})'>".format(self.description)


Base.metadata.create_all(engine)
