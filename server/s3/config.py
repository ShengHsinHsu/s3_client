import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
