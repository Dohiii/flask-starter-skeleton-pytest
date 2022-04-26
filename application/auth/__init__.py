"""
The Auth Blueprint handles the creation, modification, deletion,
and viewing of users for this application.
"""
from flask import Blueprint
auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

from . import views
