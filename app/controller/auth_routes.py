from flask import Blueprint, current_app, request
from app.schemas.serializers import UserSchema
from app.models import User

bp_users = Blueprint('user', __name__)

@bp_users.route('/', methods=['GET'])
def list():
    us = UserSchema(many=True)
    result = User.query.all()
    return us.jsonify(result)


@bp_users.route('/register', methods=['POST'])
def register():
    us = UserSchema()
    print(request.json)
    user, error = us.load(request.json)
    current_app.db.session.add(user)
    current_app.app.db.session.commit()
    return us.jsonify(user), 200
