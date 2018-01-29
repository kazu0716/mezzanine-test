Mezzanine Test
====

## Overview

Victim application in penetration test of password list attack for my understanding by using Mezzanine like "Wordpress"
http://mezzanine.jupo.org/docs/

## Requirement
- python3
- pip3
- git

## Usage

- basic usage
```
# add user list
python manage.py runscript create_users
# run by test server
python3 manage.py runserver
```

- modify user infomation
  - to add or del user_tables

```
cat scripts/create_users.py
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
```

- admin page(CMS)
  - http://127.0.0.1:8000/admin/

- Other pages
  - http://127.0.0.1:8000/

## Install

```
git clone https://github.com/kazu0716/mezzanine-test.git
cd mezzanine-test/
pip3 install -r requirement.txt
python3 manage.py createdb
python manage.py runscript create_users
python3 manage.py runserver
```
