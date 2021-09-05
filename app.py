from auth import requires_auth,AuthError
from operator import imod
from flask.json import jsonify
import flask_sqlalchemy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, render_template, request,abort,Response, flash, redirect, url_for)
from models import setup_db, Actor, Movie,db
from flask_cors import CORS
from models import *
from config import AUTH0_AUTHORIZE_URL

def create_app():

    #----------------------------------------------------------------------------#
    # App Config.
    #----------------------------------------------------------------------------#
    app = Flask(__name__)
    app.config.from_object('config')
    setup_db(app)
    migrate = Migrate(app, db)

    #----------------------------------------------------------------------------#
    # CORS Config.
    #----------------------------------------------------------------------------#
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    #----------------------------------------------------------------------------#
    # Controllers.
    #----------------------------------------------------------------------------#
    @app.route('/')
    def index():
        return render_template('index.html', AUTH0_AUTHORIZE_URL=AUTH0_AUTHORIZE_URL )

    @app.route('/loggedin')
    def loggedinCallback():
        data= request.args.get('auth_token')
        return render_template('index.html', AUTH0_AUTHORIZE_URL=AUTH0_AUTHORIZE_URL,token=data )

    @requires_auth("get:movies")
    @app.route('/movies')
    def getAllMovies():
        try:
            movies = Movie.query.all()
            if len(movies) == 0:
                abort(404)
            data =  jsonify({
                "success" : True,
                "movies" : [movie.format() for movie in movies]
            })
            return data
        except:
            abort(422)

    @app.route('/actors')
    @requires_auth("get:actors")
    def getAllActors():
        try:
            actors = Actor.query.all()
            if len(actors) == 0:
                abort(404)
            data =  jsonify({
                "success" : True,
                "actors" : [actor.format() for actor in actors]
            })
            return data
        except:
            abort(422)


    @app.route('/movies/<movieId>')
    @requires_auth("get:movies")
    def getMovie(movieId):
        try:
            movie = Movie.query.get(movieId)
            if not movie:
                abort(404)
            data =  jsonify({
                "success" : True,
                "movie" : movie.format()
            })
            return data
        except:
            abort(422)

    @app.route('/actors/<actorId>')
    @requires_auth("get:actors")
    def getActor(actorId):
        try:
            actor = Actor.query.get(actorId)
            if not actor:
                abort(404)
            data =  jsonify({
                "success" : True,
                "actor" : actor.format()
            })
            return data
        except:
            abort(422)

    @app.route('/movies/<movieId>',methods=['DELETE'])
    @requires_auth("delete:movie")
    def deleteMovie(movieId):
        try:
            movie = Movie.query.get(movieId)
            if not movie:
                abort(404)
            movie.delete()
            data =  jsonify({
                "success" : True,
                "movie" : movie.format()
            })
            return data
        except:
            abort(422)

    @app.route('/actors/<actorId>',methods=['DELETE'])
    @requires_auth("delete:actor")
    def deleteActor(actorId):
        try:
            actor = Actor.query.get(actorId)
            if not actor:
                abort(404)
            actor.delete()
            data =  jsonify({
                "success" : True,
                "actor" : actor.format()
            })
            return data
        except:
            abort(422)

    @app.route('/movies',methods=['POST'])
    @requires_auth("post:movie")
    def createMovie():
        try:
            data = request.get_json()
            movie = Movie(title = data['title'],
            release_year = data['release_year'])

            movie.insert()
            
            data =  jsonify({
                "success" : True,
                "movie" : movie.format()
            })
            return data
        except:
            abort(422)

    @app.route('/actors',methods=['POST'])
    @requires_auth("post:actor")
    def createActor():
        try:
            data = request.get_json()
            actor = Actor(name=data['name'],
            age=data['age'],gender=data['gender'])
        
            actor.insert()
            
            data =  jsonify({
                "success" : True,
                "actor" : actor.format()
            })
            return data
        except:
            abort(422)

    @app.route('/movies/<movieId>',methods=['PATCH'])
    @requires_auth("patch:movies")
    def updateMovie(movieId):
        try:
            data = request.get_json()

            movie = Movie.query.get(movieId)
            if not movie:
                abort(404)

            if 'title' in data:
                movie.title = data['title']
            if 'release_year' in data:
                movie.release_year = data['release_year']
            
            movie.update()
            
            data =  jsonify({
                "success" : True,
                "movie" : movie.format()
            })
            return data
        except:
            abort(422)

    @app.route('/actors/<actorId>',methods=['PATCH'])
    @requires_auth("patch:actors")
    def updateActor(actorId):
        try:
            data = request.get_json()

            actor = Actor.query.get(actorId)

            if not actor:
                abort(404)

            if 'name' in data:
                actor.name = data['name']
            if 'age' in data:
                actor.age = data['age']
            if 'gender' in data:
                actor.gender = data['gender']

            actor.update()
            
            data =  jsonify({
                "success" : True,
                "actor" : actor.format()
            })
            return data
        except:
            abort(422)

    @app.errorhandler(400)
    @app.errorhandler(401)
    @app.errorhandler(422)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_handler(error):
        return jsonify({
            'success': False,
            'error': error.code,
            'message': error.description
        }), error.code

    return app



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    create_app().run(debug=True)
