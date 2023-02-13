# import required modules
from app.dao.genres import GenreDao


# creating class to contain all logics from DAO class
class GenreService:

    def __init__(self, dao: GenreDao):
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

    def get_one(self, gid):
        """
        applying get_one() method to dao object

        :param gid: id of required movie
        :return:
        """
        return self.dao.get_one(gid)
