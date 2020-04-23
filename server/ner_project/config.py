import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True

    SECRET_KEY = 'hahaha dev rocks'

    DATABASE = os.path.join(basedir, '..', 'instance', 'hello_ner.sqlite')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '..', 'instance', 'hello_ner.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
