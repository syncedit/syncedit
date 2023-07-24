from flask import Blueprint

from . import bp

@bp.route('/hello')
def hello():
    return 'Hello from filehandler !!'
