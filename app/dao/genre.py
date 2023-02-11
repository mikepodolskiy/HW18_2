# creating class for interaction with db
class GenreDao:
    # creating constructor, getting object - session and save it in itself. session could be with different db type (
    # sqlit... etc)
    def __init__(self, session):
        self.session = session

    # creating methods for CRUD

    def get_all(self):
        pass

    def get_one(self, mid):
        pass
