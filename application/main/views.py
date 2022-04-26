#################
# Imports
#################
from flask import render_template
from application import db
from . import main_blueprint

################
# Views
################


@main_blueprint.route('/')
def index():
    return render_template('index.html')
