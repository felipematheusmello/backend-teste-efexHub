from flask_jwt_extended import JWTManager
from config import revoked_tokens

jwt = JWTManager()

def configure(app):
    jwt.init_app(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    return jti in revoked_tokens