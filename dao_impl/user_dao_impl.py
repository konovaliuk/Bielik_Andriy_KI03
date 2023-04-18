from models.user import User
from interfaces.user_dao import UserDao


class UserDaoImpl(UserDao):
    def __init__(self, connection_pool):
        self.cnx = connection_pool

    def read_by_id(self, user_id: int):
        query = (f"SELECT * FROM users WHERE user_id={user_id}")
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            result = User(*cursor.fetchone())
            result.print()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Скоріш за все, користувача з таким id не знайдено.")

    def add(self, user: User):
        query = (f"INSERT INTO users(user_name, user_surname, users_email, user_phone, user_password) VALUES('{user.name}', '{user.surname}', '{user.email}', '{user.phone}', '{user.password}')")
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")

    def delete(self, user_id: int):
        query = (f"DELETE FROM users WHERE user_id={user_id}")
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")