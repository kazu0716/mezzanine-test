# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User

# modify user table to add test user
user_tables = [
    {
        "user": "john",
        "mail": "john@example.com",
        "pass": "john",
    },
    {
        "user": "tom",
        "mail": "tom@example.com",
        "pass": "tom",
    },
    {
        "user": "ops",
        "mail": "ops@example.com",
        "pass": "ops",
    },
    {
        "user": "dev",
        "mail": "dev@example.com",
        "pass": "dev",
    }
]


def run():
    for user_info in user_tables:
        if not User.objects.filter(username=user_info["user"]).exists():
            user = User.objects.create_user(user_info["user"], user_info["mail"], user_info["pass"])
            user.is_superuser = True
            user.is_staff = True
            user.save()
