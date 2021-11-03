from flask import render_template, url_for, request, redirect, flash
from movie_finder import app
from movie_finder.forms import Form
from finder import search_movie, get_movie, get_cast, get_popular
from difflib import get_close_matches

@app.route("/", methods=["GET", "POST"])
def home():
    popular_movies = get_popular()
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("search_results", string=name))
    return render_template("index.html", popular_movies=popular_movies)

@app.route("/results/<string>")
def search_results(string):
    movie_list = search_movie(string)
    if len(movie_list) > 0:
        movie1 = movie_list[0]
    else:
        return redirect(url_for('home'))
    return render_template("results.html", movie_list=movie_list[1:], movie1=movie1)

@app.route("/movie/<int:id>")
def movie(id):
    movie = get_movie(id)
    cast = get_cast(id)
    return render_template("movie.html", movie=movie, cast=cast)