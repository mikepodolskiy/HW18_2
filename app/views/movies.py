# import required libraries and modules
from flask import request
from flask_restx import Namespace, Resource
from app.dao.model.movies import MovieSchema

movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        getting all movies list using method get_all of MovieDao class object
        using serialization with Schema class object
        :return: movies list(?????)
        """
        all_movies = movie_dao.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieDao class object
        :return: info message,response code
        """
        req_json = request.json
        movie_dao.create(req_json)

        return 'data added', 201


@movie_ns.route('<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        """
        getting one movie (dict????) using method get_one of MovieDao class object
        using serialization with Schema class object
        :return: movie with required id - dict(?????)
        """
        requested_movie = movie_dao.get_one(mid)
        return movie_schema.dump(requested_movie), 200


    def put(self, mid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieDao class object
        :param mid: element to update id
        :return: response code
        """
        request_data = request.json
        request_data['id'] = mid
        movie_dao.update(request_data)


        return '', 204

    def delete(self, mid):
        return '', 204