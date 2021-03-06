# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 03:35
from __future__ import unicode_literals

from django.db import migrations


def load_initial_data(app, schema_editor):
    """
    Creates the initial superadmin user for acm@mst.edu.
    """
    SIG = app.get_model("sigs", "SIG")
    User = app.get_model("accounts", "User")
    db_alias = schema_editor.connection.alias
    admin = User.objects.get(email="acm@mst.edu")
    acmgeneral = SIG.objects.create(
        id="acm-general", is_active=True, founder=admin, chair=admin
    )
    acmgeneral.save()


def reverse_initial_data(apps, schema_editor):
    """
    Reverts the creation of the initial superadmin user.
    """
    User = apps.get_model("sigs", "SIG")
    db_alias = schema_editor.connection.alias
    User.objects.using(db_alias).filter(id="acm-general").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sigs', '0001_initial'),
        ('accounts', '0002_starting_data')
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_initial_data)
    ]
