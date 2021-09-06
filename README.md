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
## Tokens:
### Assistant:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjN0cl9LM3VXdHRoVE1EOHI2QW9XWCJ9.eyJpc3MiOiJodHRwczovL3NyaTU5Nzc2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0NWQ4MDdmOWE5NTAwNzFkYzJkZWMiLCJhdWQiOiJ1c2VyIiwiaWF0IjoxNjMwOTM0MTYyLCJleHAiOjE2MzEwMDYxNjIsImF6cCI6ImhodEJ2a0FyRFowa1EweHNZRHluckt0MTdXYnZsWERFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.x_owkMCLXzzFqHkzA6oBtBOrf829GJdHqXW52llZTi2CZSkuWLRgQJDU9GLjp3ud52mRLqQVfFQ_Ze9q636Ikk9IBrxaoBIgHOJSXkdWm2XtqVfZE7qByZH664DeevHlIpLit7ml0OiHFsLMQ4r1GkaHeQ6Xsua2jhN2xt_eRxamGM2xrfUpq1U92vr-La1MriI1RQXD0Y4sDvqS_pPjdD1_69vKnEDf8fdZkD_Mg2TrhlQ23vjFEaDTJ5cfu5nTc1EfYVR5ojB81ZbrNouWx2vqY291oyM86-ngC3llJUzhXP0ciwptPVpIPltakvkJBVHGNdvd0h_OK5rueN2o6A
```
### Director:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjN0cl9LM3VXdHRoVE1EOHI2QW9XWCJ9.eyJpc3MiOiJodHRwczovL3NyaTU5Nzc2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0NjU3ZjNmMjM2MjAwNjk0ZTgxMjYiLCJhdWQiOiJ1c2VyIiwiaWF0IjoxNjMwOTM0MjA4LCJleHAiOjE2MzEwMDYyMDgsImF6cCI6ImhodEJ2a0FyRFowa1EweHNZRHluckt0MTdXYnZsWERFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiXX0.vWOHJSG_OSyMxllqCYcGkODtn-K9vuJdVi2b5VhhyihWcBV_PHw07EDAEkHdAG-xi4Dfb80wOokrIObzfVlAJ0HQTv8Ag-LURZoVGkzGyfofulfs5SMbTJf0xpFvMdMwGpanY2YoYmswV69zVNWaPZbpsYPOZIP4q4wURpLsZuC6ebiQBXa58Kk_qWRFf4_NUI9_9bY1iI75VxYUQTEyI4c2nGxFKLHwJCAnW1YAiMuSFXEprZB4SPw9cU6XVRs9v8v3EDteJUP3XV945AHg8JL6pA0_ZzpC1zQPVKpumC7lw6hYrjqOb2PQXn1z17rL8tbKDG23mLDgS7xBD9JAFA
```
### Producer
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjN0cl9LM3VXdHRoVE1EOHI2QW9XWCJ9.eyJpc3MiOiJodHRwczovL3NyaTU5Nzc2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0NjVkNmY0M2E2MjAwNmE4ZDllMWMiLCJhdWQiOiJ1c2VyIiwiaWF0IjoxNjMwOTM0MjQyLCJleHAiOjE2MzEwMDYyNDIsImF6cCI6ImhodEJ2a0FyRFowa1EweHNZRHluckt0MTdXYnZsWERFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.3YCSty7NVkyXydfLxHC1HIvmeWCBGY85cC-C0LDtuA90QwfisGEcVuLG3jaSd4SDnuP6ysEsZZUoT911eHD2nBNDMBAcIrWPrTmXux3lcgD0peaNoRTQa4tVby-HXnXuxbYv7CLd2gZJrptJWK5Qiv5osjToO5X6fnCBYfpDgAyBa3aCor65wzPeGlz2zOul7px47prDOaE6LY5m8vu5Yqv2vRx7pnYk5ONYB6nZAEWRj7LSSq7mJokEXPRKPqq2PoEl2MAfhEyvjHEJNKstaPH4FVlZPkRlzqJm_mCO2BndFVzBFyExUlX49NoqPycR4glwX1c9OLuDjKDBa-yoiw
```
