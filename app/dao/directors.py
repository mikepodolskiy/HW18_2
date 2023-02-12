# import required modules
from app.dao.model.directors import Director


# creating class for interaction with db
class DirectorDao:
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
        return self.session.query(Director).all()

    def get_one(self, did):
        """
        using session, requesting to db to required class, getting data by id
        :param did: required id
        :return: data of element with required id
        """

        return self.session.query(Director).get(did)
