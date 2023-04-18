from interfaces.book_dao import BookDao
from models.book import Book


class BookDaoImpl(BookDao):
    def __init__(self, connection_pool):
        self.cnx = connection_pool

    def read_by_id(self, book_id: int):
        query = (f"SELECT idbook, author_id, key_words, title, amount_of_pages, book_status FROM book WHERE idbook={book_id}")
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            result = Book(*cursor.fetchone())
            result.print()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Скоріш за все, книжки з таким id не існує.")

    def add(self, book: Book):
        query = f"INSERT INTO book(idbook, author_id, book_status, key_words, title, amount_of_pages) VALUES('{book.id}', '{book.author_id}', '{book.book_status}', '{book.key_words}', '{book.title}', '{book.amount_of_pages}') "
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")

    def delete(self, book_id: int):
        query = (f"DELETE FROM book WHERE idbook={book_id}")
        try:
            conn = self.cnx.get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except:
            print("Схоже, сталася помилка. Спробуйте ще раз")
