from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from flask import Blueprint, current_app, request, jsonify
from flask_cors import cross_origin
from app.schemas.serializers import UserSchema
from config import revoked_tokens
from app.models import User

bp_users = Blueprint('user', __name__)

@bp_users.route('/', methods=['GET'])
@jwt_required(refresh=True)
def list():
    us = UserSchema(many=True)
    result = User.query.all()
    return us.jsonify(result)

@bp_users.route('/register', methods=['POST'])
@cross_origin()
def register():
    try:
        us = UserSchema()
        user = us.load(request.json)
        user.set_password(str(user.password))

        current_app.db.session.add(user)
        current_app.db.session.commit()

        return us.jsonify(user), 201

    except Exception as e:
        current_app.db.session.rollback()
        return jsonify({"error": str(e)}), 400

@bp_users.route('/login', methods=['POST'])
@cross_origin()
def login():
    try:
        us = UserSchema()
        user_data = us.load(request.json)
        user = User.query.filter_by(username=str(user_data.username)).first()
        if not user or not user.check_password(request.json['password']):
            return jsonify({"error": 'Invalid password or username'}), 400

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400



@bp_users.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def logout():
    jti = get_jwt()['jti']
    revoked_tokens.add(jti)

    return jsonify(message="Logout successfully"), 200

@bp_users.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token)


@bp_users.route('/delete', methods=['DELETE'])
@jwt_required(refresh=True)
def delete():
    try:
        user_id = request.args.get('id')
        User.query.filter_by(id=user_id).delete()

        current_app.db.session.commit()
        return {'message': 'User deleted successfully'}, 204

    except Exception as e:
        return jsonify({'error': str(e)}), 400