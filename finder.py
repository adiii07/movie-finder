from tmdbv3api import TMDb, Search
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.language = 'en'
tmdb.api_key = "adffce420f0b1d17b42afac9a5dc59e3"

movie = Movie()

def search_movie(name):
    search = movie.search(name)
    return search

def get_movie(id):
    m = movie.details(id)
    return m