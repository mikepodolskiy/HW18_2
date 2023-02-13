# import required libraries and modules
from flask import Flask
from flask_restx import Api

from app.views.movies import movie_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from config import Config
from setup_db import db
from initial_data import data
from app.dao.model.movies import Movie
from app.dao.model.directors import Director
from app.dao.model.genres import Genre


# creating and configuring app in function
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# adding sqlalchemy and rest-x, adding namespaces in function
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


# function for data creation from file
def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()
        for movie in data["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            with db.session.begin():
                db.session.add(m)

        for director in data["directors"]:
            d = Director(
                id=director["pk"],
                name=director["name"],
            )
            with db.session.begin():
                db.session.add(d)

        for genre in data["genres"]:
            g = Genre(
                id=genre["pk"],
                name=genre["name"],
            )
            with db.session.begin():
                db.session.add(g)


# creating app using function
app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
