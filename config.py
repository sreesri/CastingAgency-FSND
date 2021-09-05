import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

USERNAME = os.getenv('APP_USERNAME')
PASSWORD = os.getenv('PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
TEST_DB_NAME  = os.getenv('TEST_DB_NAME')

APP_DOMAIN = os.getenv('APP_DOMAIN')
API_IDENTIFIER = os.getenv('API_IDENTIFIER')
CLIENT_ID = os.getenv('CLIENT_ID')
BASE_URL = os.getenv('BASE_URL')
CALLBACK_URL = os.getenv('CALLBACK_URL')

ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')

# Login url
AUTH0_AUTHORIZE_URL = f'https://{APP_DOMAIN}/authorize?audience={API_IDENTIFIER}&response_type=token&client_id={CLIENT_ID}&redirect_uri={BASE_URL}{CALLBACK_URL}&prompt=login'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/castingAgency'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/castingAgency'