# import required modules
from app.dao.model.movies import Movie


# creating class for interaction with db
class MovieDao:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlit... etc)
    def __init__(self, session):
        self.session = session

    # creating methods for CRUD

    def get_all(self):
        """
        using session, requesting to db to required class, getting all data
        :return: all data of required class
        """
        return self.session.query(Movie).all()

    def get_one(self, mid):
        """
        using session, requesting to db to required class, getting data by id
        :param mid: required id
        :return: data of element with required id
        """

        return self.session.query(Movie).get(mid)

    def get_by_director(self, did):
        pass

    def get_by_genre(self, gid):
        pass

    def get_by_year(self, yid):

        pass

    def create(self, data):
        """
        creating Movie class object using data
        requesting to session to add movie
        requesting to session to commit changes to save info
        :param data: data from request body
        :return: movie that was added (not necessary)
        """
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie
    def update(self, data):
        """
        getting id from data using get method (as data type is dict)
        getting movie to update using get_one with id, that was gotten
        creating fields of movie_to update with info, received from data, using get() method by field names
        requesting to session to add and commit
        :param data: data from request body
        :return: updated element (not necessary)
        """
        mid = data.get('id')
        movie_to_update = self.get_one(mid)
        movie_to_update.title = data.get('title')
        movie_to_update.description = data.get('description')
        movie_to_update.trailer = data.get('trailer')
        movie_to_update.year = data.get('year')
        movie_to_update.rating = data.get('rating')
        movie_to_update.genre_id = data.get('genre_id')
        movie_to_update.director_id = data.get('director_id')

        self.session.add(movie_to_update)
        self.session.commit()

        return movie_to_update


    def delete(self, mid):
        pass
