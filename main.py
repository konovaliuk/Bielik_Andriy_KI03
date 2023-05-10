from connection.connection_pool import MySQLConnectionPool
from DAO.dao_impl.author_dao_impl import AuthorDaoImpl
from DAO.dao_impl.book_dao_impl import BookDaoImpl
from DAO.dao_impl.user_dao_impl import UserDaoImpl
from models.user import User


def main():
    pool = MySQLConnectionPool().get_connection()
    user_table_1 = UserDaoImpl(pool)
    user_table_2 = BookDaoImpl(pool)
    user_table_3 = AuthorDaoImpl(pool)
    user_1 = User(13, "Jack", "Black", "jack_bl@gmail.com", "+380987645120", "12345")
    #user_table_1.delete(12)
    #user_table_1.add(user_1)
    #user_table_1.read_by_id(13)
    #user_table_2.read_by_id(1)
    #user_table_3.read_by_id(1)


if __name__ == "__main__":
    main()
