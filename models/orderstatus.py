from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class OrderStatus(Base):
    __tablename__ = 'order_status'
    status_id = Column(Integer, primary_key=True)
    status_situation = Column(String)
