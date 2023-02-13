# import required modules
from app.dao.model.genres import Genre


# creating class for interaction with db
class GenreDao:
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
        return self.session.query(Genre).all()

    def get_one(self, gid):
        """
        using session, requesting to db to required class, getting data by id
        :param gid: required id
        :return: data of element with required id
        """

        return self.session.query(Genre).get(gid)
