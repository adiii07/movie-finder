from flask import render_template, url_for, request, redirect
from movie_finder import app
from movie_finder.forms import Form
from finder import search_movie, get_movie

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        movie_list = search_movie(name)
        movie1 = movie_list[0]
    return render_template("index.html", movie_list=movie_list[1:], movie1=movie1)
    # return render_template("index.html")

@app.route("/movie/<int:id>")
def movie(id):
    movie = get_movie(id)
    return render_template("movie.html", movie=movie)