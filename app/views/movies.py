# import required libraries and modules
from flask import request
from flask_restx import Namespace, Resource
from app.dao.model.movies import MovieSchema

# creating namespaces for movies
movie_ns = Namespace('movies')

# creating serializators for one or many elements
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


# creating class based views using namespaces for all required endpoints
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        getting all movies list using method get_all of MovieDao class object
        using serialization with Schema class object
        :return: movies list(?????)
        """
        # director_id = request.args.get('director_id')
        # genre_id = request.args.get('genre_id')
        # year = request.args.get('year')
        # if director_id:
        #     director_movies = movie_dao.get_by_director(director_id)
        #     return movies_schema.dump(director_movies), 200
        # if genre_id:
        #     genre_movies = movie_dao.get_by_genre(genre_id)
        #     return movies_schema.dump(genre_movies), 200
        # if year:
        #     year_movies = movie_dao.get_by_year(year)
        #     return movies_schema.dump(year_movies), 200

        substring = request.query_string
        if substring:
            movies = movie_dao.get_by(substring)
            return movies_schema.dump(movies), 200

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
class MovieView(Resource):
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


    def patch(self, mid):
        """
                getting data from request, transforming data using .json
                adding id to transformed data (as it should not contain id)
                updating required element using method update_partial() of MovieDao class object
                :param mid: element to update id
                :return: response code
                """
        request_data = request.json
        request_data['id'] = mid
        movie_dao.update_partial(request_data)

        return '', 204


    def delete(self, mid):
        """
        delete movie with required id, using method delete() of MovieDao class object

        :param mid: id of required movie to be deleted
        :return: response code
        """
        movie_dao.delete(mid)

        return '', 204