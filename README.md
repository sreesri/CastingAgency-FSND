# CastingAgency-FSND
## _Final Project for Udacity FSND_
## Links:
Heroku Link: https://casting-agency-sri59776-fsnd.herokuapp.com
Local server : http://localhost:5000
## About:
Casting agency offers web based management system to create,update and delete **Actors** and **Movies**.
## Getting Started:
### Prerequisite:
#### Python 3.7 or above
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).
#### Virtual Enviornment
Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages.
## Running the server locally
#### Modify .env file:
Modify the .env file:
Change the `SQLALCHEMY_DATABASE_URI` property to point your local postgres server location
To run the server, execute:
```bash
export FLASK_APP=app.py
python app.py
```
## API Reference:
Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- Casting Assistant
  - can only view the list of artist and movies and can view complete information for any actor or movie
- Casting Director
  - All permissions a Casting `Assistant` has and…
  - Add or delete an actor from the database
- Executive Producer
  - All permissions a Casting `Director` has and…
  - Add or delete a movie from the database
## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": false
    "error": 404,
    "message": "Error Message"
}
```
The API will return the following errors based on how the request fails:
 - 400: Bad Request
 - 401: Unauthorized
 - 404: Not Found
 - 422: Unprocessable Entity
 - 500: Internal Server Error

## Endpoints
#### GET /
 - index
   - root endpoint
   - There is a provision for users to login and get the auth token.
   - Requires no authentication.
   - On click of Login user will be redirected to Auth0 page to login
 ##### Credentials:
- Casting Assistant
  emailId : assistant@cas.com
  password : Asdf1234!
- Casting Director
  emailId : director@cas.com
  password : Asdf1234!
- Executive Producer
  emailId : producer@cas.com
  password : Asdf1234!
 #### GET /actors
 - Get the list of actors in the system
   - gets the list of all the actors
   - requires `get:actors` permission
#### GET /actors/{actor_id}
 - General
   - gets the complete info for an actor
   - requires `get:actors` permission
#### GET /movies
 - General
   - gets the complete info for an movie
   - requires `get:movies` permission
#### GET /movies/{movieId}
 - General
   - gets the complete info for a movie
   - requires `get:movies` permission
#### DELETE /movies/{movieId}
 - General
   - deletes a movie
   - requires `delete:movie` permission
#### DELETE /actors/{actorId}
 - General
   - deletes an actor
   - requires `delete:actor` permission
#### POST /movies
 - General
   - creates a movie
   - requires `post:movie` permission
#### POST /actors
 - General
   - creates an actor
   - requires `post:actor` permission
#### PATCH /movies/{movieId}
 - General
   - updates a movie
   - requires `patch:movies` permission
#### PATCH /actors/{actorId}
 - General
   - updates an actor
   - requires `patch:actors` permission
