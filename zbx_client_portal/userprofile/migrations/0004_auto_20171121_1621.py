# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 13:21
from __future__ import unicode_literals
import os
import csv

from django.db import migrations

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'bad_usernames.txt'


def forwards_func(apps, schema_editor):
    names = []
    BadUsername = apps.get_model("userprofile", "BadUsername")
    db_alias = schema_editor.connection.alias
    with open(os.path.join(fixture_dir, fixture_filename)) as f:
        names = [BadUsername(username=line.strip()) for line in f]
    BadUsername.objects.using(db_alias).bulk_create(names)


def reverse_func(apps, schema_editor):
    BadUsername = apps.get_model("userprofile", "BadUsername")
    db_alias = schema_editor.connection.alias
    BadUsername.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0003_badusername'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
