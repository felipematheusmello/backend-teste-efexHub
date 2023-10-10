from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import (
    SQLALCHEMY_HOST,
    SQALCHEMY_DB_NAME,
    SQALCHEMY_DB_PASSWORD,
    SQALCHEMY_DB_USER,
    SQALCHEMY_PORT,
    APP_SECRET_KEY
)


app = Flask(__name__)

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{SQALCHEMY_DB_USER}:{SQALCHEMY_DB_PASSWORD}@{SQLALCHEMY_HOST}:{SQALCHEMY_PORT}/{SQALCHEMY_DB_NAME}'
app.config['SECRET_KEY'] = APP_SECRET_KEY

db = SQLAlchemy(app)
ma = Marshmallow(app)
