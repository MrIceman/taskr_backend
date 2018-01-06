import os

basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database.db")
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir
SECRET_KEY = 'secret!'
