# import required libraries and modules
from flask_restx import Namespace, Resource
from app.dao.model.directors import DirectorSchema
from implemented import director_service

# creating namespace
director_ns = Namespace('directors')

# creating serializers for one or many elements
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


# creating class based views using namespaces for all required endpoints
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
        getting all directors list using method get_all of DirectorDao class object
        using serialization with Schema class object
        :return: directors list
        """
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """
        getting one director dict using method get_one of DirectorDao class object
        using serialization with Schema class object
        :return: director with required id - dict(?????)
        """
        requested_director = director_service.get_one(did)
        return director_schema.dump(requested_director), 200
