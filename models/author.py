from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    author_name = Column(String)
    nationality = Column(String)

    def __init__(self, Id, Name, Nationality):
        self.author_id = Id
        self.author_name = Name
        self.nationality = Nationality

    def print(self):
        print(f" ID - {self.author_id}, Name - {self.author_name}, Nationality - {self.nationality}.")
