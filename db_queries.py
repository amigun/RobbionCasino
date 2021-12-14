from models import *


def user_register(user_id):
    User.get_or_create(user_id=user_id)


def set_owner(user_id, owner):
    user = User.get(user_id=user_id)
    user.owner = owner
    user.save()


def user_info(user_id):
    user = User.get(user_id=user_id)

    return [user.user_id, user.owner, user.count_referals, user.played, user.balance, user.demo_balance]