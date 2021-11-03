from flask import render_template, redirect, request, session
from flask_app.models import author, book
from flask_app import app
from flask_app.models import author

@app.route("/")
def index():
    return redirect("/authors")

# show all authors
@app.route("/authors")
def authors():
    return render_template("authors.html",all_authors = author.Author.getAllAuthors())

# add author
@app.route("/create",methods=["POST"])
def addAuthor():
    data = {
        "name": request.form["name"]
    }
    author.Author.createAuthor(data)
    return redirect("/authors")

# authors details page
@app.route("/author_show/<int:author_id>")
def viewAuthorDetails(author_id):
    data = {
        "author_id": author_id

    }
    return render_template("author_show.html", author = author.Author.getOneAuthor(data), favoriteBooks = author.Author.getAuthorsFavoriteBooks(data))

@app.route("/author_show/<int:book_id>")
def viewUnfavoredBooks(book_id):
    data = {
        "book_id": book_id
    }
    return render_template("author_show.html",unFavorites = author.Author.getBooksNotFavoritedByAuthor(data))
