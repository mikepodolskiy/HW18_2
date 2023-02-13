# import required classes
from app.dao.directors import DirectorDao
from app.dao.genres import GenreDao
from app.dao.movies import MovieDao
from app.service.directors import DirectorService
from app.service.genres import GenreService
from app.service.movies import MovieService
from setup_db import db

# creating Dao object for movie, with session
movie_dao = MovieDao(db.session)
# creating Service object fo movie, with movie dao object
movie_service = MovieService(movie_dao)

# creating Dao object for director, with session
director_dao = DirectorDao(db.session)
# creating Service object fo director, with director dao object
director_service = DirectorService(director_dao)

# creating Dao object for director, with session
genre_dao = GenreDao(db.session)
# creating Service object fo genre, with genre dao object
genre_service = GenreService(genre_dao)
