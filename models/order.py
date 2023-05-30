from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Order(Base):
    __tablename__ = 'order_book'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('book.idbook'))
    status_id = Column(Integer, ForeignKey('order_status.status_id'))




    def __init__(self, User_id, Book_id, Status_id):
        self.user_id = User_id
        self.book_id = Book_id
        self.status_id = Status_id

    def print(self):
        print(self.user_id, self.book_id, self.status_id)
