from flask import render_template, url_for, request, redirect
from movie_finder import app
from movie_finder.forms import Form
from finder import search_movie, get_movie, get_cast

@app.route("/", methods=["GET", "POST"])
def home():
    global movie_list
    if request.method == "POST":
        name = request.form.get("name")
        movie_list = search_movie(name)
        return redirect(url_for("search_results"))
    return render_template("index.html")

@app.route("/results")
def search_results():
    movie1 = movie_list[0]
    return render_template("results.html", movie_list=movie_list[1:], movie1=movie1)

@app.route("/movie/<int:id>")
def movie(id):
    movie = get_movie(id)
    cast = get_cast(id)
    return render_template("movie.html", movie=movie, cast=cast)