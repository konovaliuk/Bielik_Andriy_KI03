from DAO.interfaces.book_dao import BookDao
from connection.database import DatabaseConnection
from models.author import Author
from models.book import Book
from models.bookstatus import BookStatus
from models.order import Order
from models.user import User


class BookDaoImpl(BookDao):
    def __init__(self):
        self.cnx = DatabaseConnection().get_session()

    def read_by_id(self, book_id: int):
        try:
            result = self.cnx.query(Author.author_name, Author.nationality, BookStatus.status_situation,
                                    Book.idbook, Book.key_words, Book.title, Book.amount_of_pages) \
                .join(Author, Book.author_id == Author.author_id) \
                .join(BookStatus, Book.book_status == BookStatus.status_id) \
                .filter(Book.idbook == book_id).one()
            book = Book(*result)
            return book
        except:
            return None

    def check_book(self, book_id: int):
        try:
            book = self.cnx.query(Book).filter(Book.idbook == book_id).first()
            if book:
                return book.book_status
            else:
                return None
        except:
            return None

    def get_books(self):
        try:
            query = self.cnx.query(Author.author_name, Author.nationality, BookStatus.status_situation,
                                          Book.idbook, Book.key_words, Book.title, Book.amount_of_pages) \
                .join(Author, Book.author_id == Author.author_id) \
                .join(BookStatus, Book.book_status == BookStatus.status_id)
            books = [Book(*row) for row in query]
            return books
        except:
            raise Exception

    def get_books_with_id(self, user_id: int):
        try:
            query = self.cnx.query(Author.author_name, Author.nationality, BookStatus.status_situation,
                                          Book.idbook, Book.key_words, Book.title, Book.amount_of_pages) \
                .select_from(Order) \
                .join(Book, Book.idbook == Order.book_id) \
                .join(Author, Author.author_id == Book.author_id) \
                .join(BookStatus, BookStatus.status_id == Book.book_status) \
                .join(User, User.user_id == Order.user_id) \
                .filter(Order.user_id == user_id)
            books = [Book(*row) for row in query]
            return books
        except:
            raise Exception

    def add(self, book: Book):
        try:
            self.cnx.add(book)
            self.cnx.commit()
        except:
            raise Exception

    def delete(self, book_id: int):
        try:
            book = self.read_by_id(book_id)
            if book:
                self.cnx.delete(book)
                self.cnx.commit()
        except:
            raise Exception()
