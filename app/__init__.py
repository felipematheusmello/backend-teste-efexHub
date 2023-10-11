from flask import Flask
from config import (
    URI_BASE,
    APP_SECRET_KEY
)
from flask_migrate import Migrate
from app.models import configure as config_db
from app.schemas.serializers import configure as config_ma


def create_app():
    app = Flask(__name__)

    # Configuração do SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{URI_BASE}'
    app.config['SECRET_KEY'] = APP_SECRET_KEY

    config_db(app)
    config_ma(app)
    Migrate(app, app.db)

    from app.controller.auth_routes import bp_users

    app.register_blueprint(bp_users)

    return app
