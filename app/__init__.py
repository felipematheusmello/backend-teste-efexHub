from flask import Flask
from config import (
    URI_BASE,
    APP_SECRET_KEY,
    JWT_SECRET_KEY
)
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import configure as config_db
from app.schemas.serializers import configure as config_ma
from app.controller.auth import configure as config_jwt

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})
    # Configuração do SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{URI_BASE}'
    app.config['SECRET_KEY'] = APP_SECRET_KEY
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 30 * 24 * 3600 # 30 days

    config_db(app)
    config_ma(app)
    config_jwt(app)

    Migrate(app, app.db)

    from app.controller.auth_routes import bp_users
    from app.controller.task_app_routes import bp_task

    app.register_blueprint(bp_task, url_prefix='/task')
    app.register_blueprint(bp_users)

    return app
