import hashlib
from flask import session
from sqlalchemy.exc import SQLAlchemyError
from DAO.dao_impl.user_dao_impl import UserDaoImpl
from connection.database import DatabaseConnection
from models.user import User


class UserService:
    def __init__(self):
        pass

    def register(self, name, surname, email, phone, password):
        db_session = DatabaseConnection().get_session()
        user_table = UserDaoImpl(db_session)
        try:
            db_session.begin()              # Початок транзакції
            if user_table.read_by_email(email) is not None:
                return False, None, "Схоже, користувач з таким email вже існує. Спробуйте ще раз."
            if user_table.read_by_phone(phone) is not None:
                return False, None, "Схоже, користувач з таким номером телефону вже існує. Спробуйте ще раз."
            user = User.create(name, surname, email, phone, password)
            user_table.add(user)
            user_to_dict = user_table.read_by_phone(phone)
            session['user'] = user_to_dict.to_dict()
            db_session.commit()             # Збереження транзакції
            return True, None, None
        except SQLAlchemyError as err:
            db_session.rollback()           # Відкат транзакції
            return False, None, str(err)
        finally:
            db_session.close()

    def authorization(self, email, password):
        db_session = DatabaseConnection().get_session()
        user_table = UserDaoImpl(db_session)
        try:
            db_session.begin()              # Початок транзакції
            user = user_table.read_by_email(email)
            if user is None:
                return False, None, "Схоже, ви ввели неправильну email адресу. Спробуйте ще раз."
            if user.get_pass() != hashlib.md5(password.encode()).hexdigest():
                return False, None, "Схоже, ви ввели неправильний пароль. Спробуйте ще раз."
            session['user'] = user.to_dict()
            if user.get_role() == 1:
                return True, 1, None
            if user.get_role() == 2:
                return True, 2, None
            db_session.commit()             # Збереження транзакції
        except SQLAlchemyError as err:
            db_session.rollback()           # Відкат транзакції
            return False, None, str(err)
        finally:
            db_session.close()
