from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(DateTime)

    def __repr__(self):
        return "<Book(name='%s', release_date='%s')>" % \
            (self.name, self.release_date)

    @classmethod
    def get_id(cls):
        return Book.id

    @classmethod
    def find_by_id(cls, session, book_id):
        return session.query(Book).filter(Book.id == book_id).one()


