from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class BookStatus(Base):
    __tablename__ = 'book_status'
    status_id = Column(Integer, primary_key=True)
    status_situation = Column(String)
