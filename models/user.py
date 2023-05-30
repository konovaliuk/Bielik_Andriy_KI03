import hashlib
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_surname = Column(String)
    users_email = Column(String)
    user_phone = Column(String)
    user_password = Column(String)
    user_role_id = Column(Integer)

    def __init__(self, user_id, user_name, user_surname, user_email, user_phone, user_password, user_role_id):
        self.user_id = user_id
        self.user_name = user_name
        self.user_surname = user_surname
        self.users_email = user_email
        self.user_phone = user_phone
        self.user_password = user_password
        self.user_role_id = user_role_id

    @classmethod
    def create(cls, user_name, user_surname, user_email, user_phone, user_password, user_id=0, user_role_id=1):
        return cls(user_id, user_name, user_surname, user_email, user_phone, user_password, user_role_id)

    def to_dict(self):
        return {
            'id': self.user_id,
            'name': self.user_name,
            'surname': self.user_surname,
            'email': self.users_email,
            'phone': self.user_phone,
            'password': self.user_password,
            'role': self.user_role_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['name'], data['surname'], data['email'], data['phone'], data['password'],
                   data['role'])

    def get_id(self):
        return self.user_id

    def get_pass(self):
        return self.user_password

    def get_phone(self):
        return self.user_phone

    def get_role(self):
        return self.user_role_id

    def update_pass(self):
        self.user_password = hashlib.md5(self.user_password.encode()).hexdigest()