# import required libraries and modules
from flask_restx import Namespace, Resource
from app.dao.model.genres import GenreSchema
from implemented import genre_service

# creating namespace
genre_ns = Namespace('genres')

# creating serializers for one or many elements
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


# creating class based views using namespaces for all required endpoints
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        getting all genres list using method get_all of GenreDao class object
        using serialization with Schema class object
        :return: genres list
        """
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        """
        getting one genre dict using method get_one of GenreDao class object
        using serialization with Schema class object
        :return: genre with required id - dict
        """
        requested_genre = genre_service.get_one(gid)
        return genre_schema.dump(requested_genre), 200
