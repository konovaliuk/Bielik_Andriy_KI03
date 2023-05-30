from abc import ABC, abstractmethod


class AuthorDao(ABC):
    @abstractmethod
    def read_by_id(self, author_id: int):
        pass

    @abstractmethod
    def add(self, obj: object):
        pass

    @abstractmethod
    def delete(self, author_id: int):
        pass