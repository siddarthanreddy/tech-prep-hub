import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'your-secret-key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.d')
SQLALCHEMY_TRACK_MODIFICATIONS = False
