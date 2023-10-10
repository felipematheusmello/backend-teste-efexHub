import os
import secrets
from dotenv import load_dotenv

load_dotenv()
APP_SECRET_KEY = secrets.token_hex(16)
SQLALCHEMY_HOST = os.getenv('SQLALCHEMY_HOST')
SQALCHEMY_PORT= os.getenv('SQALCHEMY_PORT')
SQALCHEMY_DB_USER= os.getenv('SQALCHEMY_DB_USER')
SQALCHEMY_DB_PASSWORD= os.getenv('SQALCHEMY_DB_PASSWORD')
SQALCHEMY_DB_NAME= os.getenv('SQALCHEMY_DB_NAME')