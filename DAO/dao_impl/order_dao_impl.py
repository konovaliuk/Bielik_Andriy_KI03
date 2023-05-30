from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from DAO.interfaces.order_dao import OrderDao
from connection.database import DatabaseConnection
from models.order import Order


class OrderDaoImpl(OrderDao):
    def __init__(self):
        self.cnx = DatabaseConnection().get_session()

    def create(self, order: Order):
        try:
            insert_query = text(
                "INSERT INTO order_book(user_id, book_id, status_id, date_created) VALUES(:user_id, :book_id, "
                ":status_id, CURRENT_DATE())")
            update_query = text("UPDATE book SET book_status = 2 WHERE idbook = :book_id")
            self.cnx.execute(insert_query,
                             {"user_id": order.user_id, "book_id": order.book_id, "status_id": order.status_id})
            self.cnx.execute(update_query, {"book_id": order.book_id})
            self.cnx.commit()
        except SQLAlchemyError as err:
            self.cnx.rollback()
            raise err