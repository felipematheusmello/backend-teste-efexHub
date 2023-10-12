from flask_marshmallow import Marshmallow
from app.models import User, Task

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        include_fk = True

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True