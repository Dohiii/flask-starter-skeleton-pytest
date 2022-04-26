from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
# from flask_login import LoginManager


#######################
# Configuration
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()

# login = LoginManager()
# login.login_view = "users.login"


######################################
# Application Factory Function
######################################

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    api = Api(app)
    initialize_extensions(app)
    register_blueprints(app)
    api_add_resource(api)
    return app


##########################
# Helper Functions
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)

    db.init_app(app)
    # login.init_app(app)

    # Flask-Login configuration
    '''
    from project.models import User, Post

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()
    '''


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)

    from application.auth import auth_blueprint
    from application.main import main_blueprint
    from application.api import api_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)


def api_add_resource(api):
    from application.api.v0.items import Item
    api.add_resource(Item, '/item/<string:name>')


