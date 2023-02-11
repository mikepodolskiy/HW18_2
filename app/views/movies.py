from flask_restx import Namespace, Resource

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return 'get all', 200

    def post(self):
        return 'added', 201


@movie_ns.route('<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        return 'get one', 200


    def put(self, mid):
        return '', 204

    def delete(self, mid):
        return '', 204