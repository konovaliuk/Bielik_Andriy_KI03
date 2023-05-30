from DAO.interfaces.author_dao import AuthorDao
from connection.database import DatabaseConnection
from models.author import Author


class AuthorDaoImpl(AuthorDao):
    def __init__(self):
        self.cnx = DatabaseConnection().get_session()

    def read_by_id(self, author_id: int):
        try:
            return self.cnx.query(Author).filter(Author.author_id == author_id).first()
        except:
            print("Схоже, сталася помилка. Скоріш за все, автора з таким id не знайдено.")
            return None

    def add(self, author: Author):
        try:
            self.cnx.add(author)
            self.cnx.commit()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")

    def delete(self, author_id: int):
        try:
            author = self.read_by_id(author_id)
            if author:
                self.cnx.delete(author)
                self.cnx.commit()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")