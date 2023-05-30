from abc import ABC, abstractmethod


class UserDao(ABC):
    @abstractmethod
    def read_by_id(self, user_id: int):
        pass

    @abstractmethod
    def read_by_email(self, users_email: str):
        pass

    @abstractmethod
    def read_by_phone(self, user_phone: str):
        pass

    @abstractmethod
    def add(self, obj: object):
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass
