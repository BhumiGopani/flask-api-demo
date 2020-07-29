from flask_marshmallow import Marshmallow
from models import User, Puppy

ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        model = User


user_schema = UserSchema()


class PuppySchema(ma.Schema):
    class Meta:
        model = Puppy
        fields = ["id", "slug", "name", "image_url"]


puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)
 
