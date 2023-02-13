# import required modules
from app.dao.movies import MovieDao


# creating class to contain logics from DAO class
class MovieService:

    def __init__(self, dao: MovieDao):
        """
        creating constructor, getting dao object inside itself
        :param dao: dao object
        """
        self.dao = dao

    def get_all(self):
        """
        applying get_all() method to dao object
        :return:
        """
        return self.dao.get_all()
    def get_one(self, mid):
        """
        applying get_one() method to dao object

        :param mid: id of required movie
        :return:
        """
        return self.dao.get_one(mid)

    def get_by(self, substring):
        return self.dao.get_by(substring)


    def create(self, data):
        """
        applying create() method to dao object, using data form response
        :param data:
        :return:
        """
        return self.dao.create(data)


    def update(self, data):
        """
        getting id from data using get method (as data type is dict)
        getting movie to update using get_one with id, that was gotten
        creating fields of movie_to update with info, received from data, using get() method by field names
        :param data: data from request body
        :return:
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

        self.dao.update(movie_to_update)

    def update_partial(self, data):
        """
        getting id from data using get method (as data type is dict)
        getting movie to update using get_one with id, that was gotten
        checking what fields to update in data creating fields of movie_to update with info, received from data,
        using get() method by field names
        :param data: data from request body
        :return:
        """
        mid = data.get('id')
        movie_to_update = self.get_one(mid)
        if 'title' in data:
            movie_to_update.title = data.get('title')
        if 'description' in data:
            movie_to_update.description = data.get('description')
        if 'trailer' in data:
            movie_to_update.trailer = data.get('trailer')
        if 'year' in data:
            movie_to_update.year = data.get('year')
        if 'rating' in data:
            movie_to_update.rating = data.get('rating')
        if 'genre_id' in data:
            movie_to_update.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie_to_update.director_id = data.get('director_id')

        self.dao.update(movie_to_update)
    def delete(self, mid):
        self.dao.delete(mid)
