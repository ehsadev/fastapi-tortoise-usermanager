# app/models/user.py
from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    is_admin = fields.BooleanField(default=False)
    is_verify = fields.BooleanField(default=True)

    class Meta:
        table = "users"
