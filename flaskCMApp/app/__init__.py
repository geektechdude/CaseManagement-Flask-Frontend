from flask import Flask


def create_app():

    # creates app
    app = Flask(__name__)

    # adds blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app