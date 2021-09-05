from config import ASSISTANT_TOKEN,  DIRECTOR_TOKEN, PASSWORD, SQLALCHEMY_DATABASE_URI, TEST_DB_NAME, USERNAME
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie
from app import create_app


class CastingAgencyUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        print(self.client)
        self.database_name = TEST_DB_NAME
        database_user = USERNAME
        database_pass = PASSWORD
        self.database_path = SQLALCHEMY_DATABASE_URI
        setup_db(self.app, self.database_path)

        self.VALID_ACTOR = {
            "name": "asdfgh",
            "age": 25,
            "gender": "male"
        }

        self.INVALID_ACTOR = {
            "name": "Ana de Armas"
        }

        self.VALID_UPDATE_ACTOR = {
            "name": "asdfgh"
        }

        self.INVALID_UPDATE_ACTOR = {}

        self.VALID_MOVIE = {
            "title": "abdfgesh",
            "release_year": 2016
        }

        self.INVALID_MOVIE = {
            "title": "abdfgesh"
        }

        self.VALID_UPDATE_MOVIE = {
            "release_year": 6.5
        }

        self.INVALID_UPDATE_MOVIE = {}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors_without_token(self):

        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Authorization Header is missing.")

    def test_get_actors(self):

        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data))
        self.assertTrue(data["success"])
        self.assertIn('actors', data)
        self.assertTrue(len(data["actors"]))

    def test_get_actors_by_id(self):

        res = self.client().get('/actors/1', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)
        self.assertIn('name', data['actor'])

    def test_404_get_actors_by_id(self):

        res = self.client().get('/actors/100', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertIn('message', data)

    def test_create_actor_with_assistant_token(self):

        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }, json=self.VALID_ACTOR)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    def test_create_actor_with_director_token(self):

        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }, json=self.VALID_ACTOR)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)

    def test_update_actor_with_assistant_token(self):

        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }, json=self.VALID_UPDATE_ACTOR)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    def test_update_actor_with_director_token(self):

        res = self.client().patch('/actors/1', headers={
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }, json=self.VALID_UPDATE_ACTOR)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)
        self.assertEqual(data["actor"]["name"],
                         self.VALID_UPDATE_ACTOR["name"])
        
    def test_delete_actor_with_assistant_token(self):
        
        res = self.client().delete('/actors/5', headers={
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    def test_delete_actor(self):
        
        res = self.client().delete('/actors/5', headers={
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)

    def test_404_delete_actor(self):
        
        res = self.client().delete('/actors/100', headers={
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertIn('message', data)


if __name__ == "__main__":
    unittest.main()
