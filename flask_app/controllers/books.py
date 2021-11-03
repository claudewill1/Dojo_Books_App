from flask import render_template, redirect, request, session
from flask_app.models import author, book
from flask_app import app

@app.route("/books")
def books():
    return render_template("books.html",book.Book.getAllBooks())

# add book
@app.route("/create/book",methods=["POST"])
def addBook():
    print(request.form)
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    book.Book.addBook.save(data)
    return redirect("/books")

# show book
@app.route("/books/<int:id>")
def showSingleBook(id):
    data = {
        "id": id
    }
    return render_template("book_show.html", book = book.Book.getSingleBook(data), authorsUnfavorited = author.Author.getAuthorsFavoriteBooks)

@app.route("/join/author",methods=["POST"])
def addAuthorFavList():
    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }
    author.Author.addFavoriteBook(data)
    return redirect(f"/book/{request.form['book_id']}")
