from marshmallow import fields
from app.app import ma
from app.schemas.task_schema import TaskSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    tasks = fields.Nested(TaskSchema, many=True, exclude=("user"))