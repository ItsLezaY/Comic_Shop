import os
from dotenv import load_dotenv #load env variables
from datetime import timedelta 





basedir = os.path.abspath(os.path.dirname(__file__)) #root folder

load_dotenv(os.path.join(basedir, '.env')) #point to direction of env variables



class Config(): 

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or "osca suki ojitos bellamy ace"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)