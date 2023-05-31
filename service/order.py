from sqlalchemy.exc import SQLAlchemyError
from DAO.dao_impl.book_dao_impl import BookDaoImpl
from DAO.dao_impl.order_dao_impl import OrderDaoImpl
from connection.database import DatabaseConnection
from models.order import Order


class OrderService:
    def __init__(self):
        pass

    def make_order(self, book_id, user_id):
        db_session = DatabaseConnection().get_session()
        book_table = BookDaoImpl(db_session)
        order_table = OrderDaoImpl(db_session)
        try:
            db_session.begin()  # Початок транзакції
            if book_table.read_by_id(book_id) is None:
                return False, None, "Схоже, ви Ввели ID книжки, якої в нас немає"
            if book_table.check_book(book_id) == 2:
                return False, None, "Схоже, ви Ввели ID книжки, яку вже хтось взяв почитати"
            order = Order(user_id, book_id, 1)
            order_table.create(order)
            db_session.commit()  # Збереження транзакції
            return True, None, "Ви успішно замовили книжку."
        except SQLAlchemyError as e:
            db_session.rollback()  # Відкат транзакції
            return False, None, str(e)
        finally:
            db_session.close()
