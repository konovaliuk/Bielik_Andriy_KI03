from DAO.interfaces.user_dao import UserDao
from connection.database import DatabaseConnection
from models.user import User


class UserDaoImpl(UserDao):
    def __init__(self):
        self.cnx = DatabaseConnection().get_session()

    def read_by_id(self, user_id: int):
        try:
            return self.cnx.query(User).filter(User.user_id == user_id).first()
        except:
            return None

    def read_by_email(self, users_email: str):
        try:
            return self.cnx.query(User).filter(User.users_email == users_email).first()
        except:
            return None

    def read_by_phone(self, user_phone: str):
        try:
            return self.cnx.query(User).filter(User.user_phone == user_phone).first()
        except:
            return None

    def add(self, user: User):
        try:
            user.update_pass()
            self.cnx.add(user)
            self.cnx.commit()
        except:
            raise Exception()

    def delete(self, user_id: int):
        try:
            user = self.read_by_id(user_id)
            if user:
                self.cnx.delete(user)
                self.cnx.commit()
        except:
            raise Exception()
