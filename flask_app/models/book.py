from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    db = "books"
    def __init__(self,data) -> None:
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favoriteAuthors = []


    # add book to database
    @classmethod
    def addBook(cls,data):
        query = "INSERT INTO books (title,num_of_pages,created_at,updated_at) VALUES (%(title)s,%(num_of_pages)s, NOW(), NOW()"

    @classmethod
    def getAllBooks(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod 
    def getSingleBook(cls,id):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        data = {
            "id": id
        }
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def getAuthorsWhoFavoriteBook(cls,id):
        query = "SELECT * FROM authors AS a ON favorites AS f ON f.author_id = a.id LEFT JOIN books AS b ON f.book_id = b.id WHERE a.id = %(id)s;"
        data = {
            "id": id
        }
        results = connectToMySQL(cls.db).query_db(query,data)
        authors = cls(results[0])
        for row_in_db in results:
            author_data = {
                "id": row_in_db["authors.id"],
                "name": row_in_db["authors.name"]
            }
        authors.favoriteAuthors.append(author.Author(author_data))
        return authors
