from models import *


def user_register(user_id):
    User.get_or_create(user_id=user_id)


def set_owner(user_id, owner):
    user = User.get(user_id=user_id)
    user.owner = owner
    user.save()