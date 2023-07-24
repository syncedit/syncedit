from flask import Blueprint

bp = Blueprint('filehandler', __name__, url_prefix='/api/v1/filehandler')

from . import models
from . import routes
