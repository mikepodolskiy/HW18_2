# import required modules
from app.dao.model.movies import Movie


# creating class for interaction with db
class MovieDao:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlite... etc)
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

    def get_by(self, substring):

        data_preliminary = dict([(item.split('=')) for item in str(substring).split('&')])
        data = {k: int(v.replace("'", "")) for k, v in data_preliminary.items()}
        print(data)

        if 'director_id' in data.keys():
            did = data['director_id']
            return self.session.query.filter(Movie.director_id == did)

        if 'genre_id' in data.keys():
            gid = data['genre_id']
            return self.session.query.filter(Movie.genre_id == gid)

        if 'year' in data.keys():
            y = data['year']
            return self.session.query.filter(Movie.year == y)


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
    def update(self, movie_to_update):
        """
        requesting to session to add movie and commit
        :param data: data from request body
        :return: updated element (not necessary)
        """

        self.session.add(movie_to_update)
        self.session.commit()

        return movie_to_update



    def delete(self, mid):
        """
        getting movie to delete using get_one with id
        :param mid: id of required movie
        :return: nothing
        """
        movie_to_delete = self.get_one(mid)
        self.session.delete(movie_to_delete)
        self.session.commit()
