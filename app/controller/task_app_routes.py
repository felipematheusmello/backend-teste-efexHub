from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Task
from app.schemas.serializers import TaskSchema
from flask_cors import cross_origin
from flask import Blueprint, current_app, request, jsonify

bp_task = Blueprint('task', __name__)

@bp_task.route('/', methods=['GET'])
@jwt_required()
@cross_origin()
def list():
    ts = TaskSchema(many=True)
    user_id = get_jwt_identity()
    if user_id:
        result = Task.query.filter_by(user_id=user_id)
        return ts.jsonify(result)

    result = Task.query.all()

    return ts.jsonify(result)

@bp_task.route('/', methods=['POST'])
@jwt_required()
@cross_origin()
def create():
    user_id = get_jwt_identity()
    try:
        ts = TaskSchema()
        data = request.json
        data['user_id'] = user_id
        task = ts.load(data)

        current_app.db.session.add(task)
        current_app.db.session.commit()

        return ts.jsonify(task), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@bp_task.route('/', methods=['PUT'])
@jwt_required()
@cross_origin()
def change():
    user_id = get_jwt_identity()
    task_id = request.args.get('id')
    try:
        ts = TaskSchema()
        data = request.json
        data['user_id'] = user_id

        task = Task.query.get(task_id)
        if not task:
            return jsonify({'error': "Task not found"}), 404

        elif task.user_id != user_id:
            return jsonify({'error': "Task is not by user"}), 404

        updated_task = ts.load(data, instance=task)
        current_app.db.session.commit()


        return ts.jsonify(updated_task), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@bp_task.route('/', methods=['DELETE'])
@jwt_required()
@cross_origin()
def delete():
    task_id = request.args.get('id')
    try:
        Task.query.filter_by(id=task_id).delete()

        current_app.db.session.commit()
        return {'message': 'Task deleted successfully'}, 204

    except Exception as e:
        return jsonify({'error': str(e)}), 400