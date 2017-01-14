from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model import Book

Base = declarative_base()
class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id))
    review = Column(String)
    rating = Column(Integer)

    def __repr__(self):
        return "<Review(review='%s', rating=%d)>" % \
            (self.review, self.rating)

    @classmethod
    def get_id(cls):
        return Review.id

    @classmethod
    def find_by_book_id(cls, session, book_id):
        query = session.query(Review).filter(Review.book_id == book_id)
        return query.all()
