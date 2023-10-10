from marshmallow import fields
from app.app import ma

class TaskSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    user_id = fields.Int()