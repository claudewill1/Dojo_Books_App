from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app import app
class Author:
    db = "books"
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favorite_books = []
        self.unfavoriteBooks = []
    @classmethod
    def createAuthor(cls,data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def getAllAuthors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def getOneAuthor(cls,id):
        query = "SELECT * FROM authors where id = %(id)s;"
        data = {
            "id": id
        }
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def getAuthorsFavoriteBooks(cls,id):
        query = "SELECT * FROM books AS b LEFT JOIN favorites AS f ON f.book_id = b.id LEFT JOIN authors AS a ON f.author_id = a.id WHERE b.id = %(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL(cls.db).query_db(query,data)
        books = cls(results[0])
        for row_from_db in results:
            favorites_data = {
                "id": row_from_db["books.id"],
                "title": row_from_db["books.title"],
                "pages": row_from_db["books.num_of_pages"]
            }
        books.favorite_books.append(book.Book(favorites_data))

        return books

    @classmethod
    def getBooksNotFavoritedByAuthor(cls,id):
        query = "SELECT title FROM books AS b LEFT JOIN favorites AS f ON f.book_id = b.id LEFT JOIN authors AS a on f.author_id = a.id WHERE  b.id = %(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL(cls.db).query_db(query,data)
        books = cls(results[0])
        for row_from_db in results:
            unfavorites = {
                "id": row_from_db["books.id"],
                "title": row_from_db["books.title"]
            }
        if unfavorites not in cls.favorite_books:
            books.unfavoriteBooks.append(unfavorites)
        return books

