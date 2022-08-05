from flask import Flask
from database import database

# blueprint import
from apps.blueprint1.views import blueprint1


def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')

    # setup all our dependencies
    database.init_app(app)

    # register blueprint
    app.register_blueprint(blueprint1, url_prefix="/blue1")

    return app


if __name__ == "__main__":
    create_app().run()