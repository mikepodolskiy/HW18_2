from flask_restx import Namespace, Resource

director_ns = Namespace('directors')

@director_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return 'get all', 200




@director_ns.route('<int:did>')
class MoviesView(Resource):
    def get(self, did):
        return 'get one', 200