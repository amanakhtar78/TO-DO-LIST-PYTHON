from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .db import init_db, close_db
from .tasks import tasks_bp

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration from environment variables
    app.config.from_mapping(      
        FLASK_ENV='development',
        FLASK_DEBUG=True
    )

    # Initialize CORS
    CORS(app)

    # Initialize Swagger
    Swagger(app)

    # Initialize the database
    with app.app_context():
        init_db()

    # Register the tasks blueprint
    app.register_blueprint(tasks_bp)

    # Register error handlers and close the db after each request
    app.teardown_appcontext(close_db)

    return app
