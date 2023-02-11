from flask_restx import Namespace, Resource

genre_ns = Namespace('genres')

@genre_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return 'get all', 200




@genre_ns.route('<int:gid>')
class MoviesView(Resource):
    def get(self, gid):
        return 'get one', 200
