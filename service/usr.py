import hashlib
from connection.connection_pool import MySQLConnectionPool
from DAO.dao_impl.user_dao_impl import UserDaoImpl
from models.user import User


class UserService:
    def register(self, name, surname, email, phone, password):
        pool = MySQLConnectionPool().get_connection()
        user_table = UserDaoImpl(pool)
        if user_table.read_by_email(email) is not None:
            print("Схоже, користувач з таким email вже існує. Спробуйте ще раз.")
            return 1
        if user_table.read_by_phone(phone) is not None:
            print("Схоже, користувач з таким номером телефону вже існує. Спробуйте ще раз.")
            return 2
        user = User.create(name, surname, email, phone, password)
        try:
            user_table.add(user)
            return 5
        except:
            return 3
        # if hashlib.md5(password.encode()).hexdigest() != user.password:
        #    print("Схоже, ви ввели неправильний пароль.")
        # user.print()
        # return user
