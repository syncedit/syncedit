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
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # Make sure the app instance directory exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        config = f'syncedit.config.{os.getenv("FLASK_ENV").title()}Config'
        app.config.from_object(config)
        app.config.from_envvar('FLASK_CONFIG')
    else:
        app.config.from_mapping(test_config)

    # Initialize database
    db.init_app(app)
    import syncedit.models as m

    with app.app_context():
        db.create_all()


    # simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'


    # page with image that can show/hide (javascript)
    @app.route('/showhide/<username>')
    def js_page(username):
        return render_template('index.html',
                               the_title='Try Out JS',
                               name=username)


    # show the app's users
    @app.route('/users')
    def show_users():
        users = [str(user) for user in m.User.query.all()]
        return users


    # make a new user
    @app.route('/reg/<username>')
    def add_user(username):
        user = m.User(username, 'letscode', 'someone@example.com')
        db.session.add(user)
        db.session.commit()
        return f'Created {username}'


    return app
