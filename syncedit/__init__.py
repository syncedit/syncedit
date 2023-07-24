"""Contains the application factory."""
import os

from flask import Flask, render_template

import syncedit.config
from syncedit.extensions import db

def create_app(test_config=None):
    """Create and configure the app.
    Read mapping test_config if it is passed, otherwise use
    instance config.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Set some defaults.
    # app.config.from_mapping(
    #     SECRET_KEY='### please-override-in-production ###'
    # )

    # Make sure the app instance directory exists.
    try:
        os.makedirs(app.instance_path)
    except FileExistsError:
        pass

    if test_config is None:
        config = f'syncedit.config.{os.getenv("FLASK_ENV").title()}Config'
        app.config.from_object(config)
        app.config.from_envvar('FLASK_CONFIG')
    else:
        app.config.from_mapping(test_config)

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()

    from syncedit.filehandler import bp as filehandler
    app.register_blueprint(filehandler)

    from syncedit.auth import bp as auth
    app.register_blueprint(auth)

    return app
