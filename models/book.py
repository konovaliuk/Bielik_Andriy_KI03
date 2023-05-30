from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    idbook = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    book_status = Column(Integer, ForeignKey('book_status.status_id'))
    key_words = Column(String)
    title = Column(String)
    amount_of_pages = Column(Integer)

    def __init__(self, Author_Name, Author_nationality, Status, ID, Key_words, Title, Amount_of_pages):
        self.author_name = Author_Name
        self.nationality = Author_nationality
        self.book_status = Status
        self.idbook = ID
        self.key_words = Key_words
        self.title = Title
        self.amount_of_pages = Amount_of_pages

    def print(self):
        print(self.author_name, self.nationality, self.book_status, self.key_words, self.title, self.amount_of_pages)
