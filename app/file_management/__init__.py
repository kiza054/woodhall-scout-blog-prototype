from flask import Blueprint

bp = Blueprint('file_management', __name__)

from app.file_management import routes