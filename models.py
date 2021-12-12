from peewee import *

db = SqliteDatabase('database.db')

class User(Model):
    user_id = IntegerField()
    owner = IntegerField(default=0)
    count_referals = IntegerField(default=0)
    played = IntegerField(default=0)
    balance = IntegerField(default=0)
    demo_balance = IntegerField(default=10000)

    class Meta:
        database = db


User.create_table()