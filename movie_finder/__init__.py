from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3c2cec5ae6c73a42552649c82e493b3a'

from movie_finder import routes