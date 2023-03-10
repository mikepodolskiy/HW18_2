# import required libraries and modules
from flask import request
from flask_restx import Namespace, Resource
from app.dao.model.movies import MovieSchema
from implemented import movie_service

# creating namespaces for movies
movie_ns = Namespace('movies')

# creating serializers for one or many elements
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


# creating class based views using namespaces for all required endpoints
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        getting all movies list or movies with filter using method get_all of MovieService class object
        using serialization with Schema class object
        :return: movies list
        """
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {'director_id': director,
                   'genre_id': genre,
                   'year': year
                   }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    def post(self):
        """
        getting data from request, transforming data using .json
        creating new element using create(transformed data) method for MovieService class object
        :return: info message,response code
        """
        req_json = request.json
        movie_service.create(req_json)

        return 'data added ', 201, {"location": f"/movies/{req_json['id']}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """
        getting one movie using method get_one of MovieService class object
        using serialization with Schema class object
        :return: movie with required id - dict
        """
        requested_movie = movie_service.get_one(mid)
        return movie_schema.dump(requested_movie), 200

    def put(self, mid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update() of MovieService class object
        :param mid: element to update id
        :return: response code
        """
        request_data = request.json
        request_data['id'] = mid
        movie_service.update(request_data)

        return '', 204

    def patch(self, mid):
        """
        getting data from request, transforming data using .json
        adding id to transformed data (as it should not contain id)
        updating required element using method update_partial() of MovieService class object
        :param mid: element to update id
        :return: response code
        """
        request_data = request.json
        request_data['id'] = mid
        movie_service.update_partial(request_data)

        return '', 204

    def delete(self, mid):
        """
        delete movie with required id, using method delete() of MovieService class object

        :param mid: id of required movie to be deleted
        :return: response code
        """
        movie_service.delete(mid)

        return '', 204
