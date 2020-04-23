import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from .config import Config

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'hello_ner.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # initiates SQL Alchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    from . import models

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # from . import db
    # db.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    from . import project
    app.register_blueprint(project.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    # enable CORS
    CORS(app)

    return app
