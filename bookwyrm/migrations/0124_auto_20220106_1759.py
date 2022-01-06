# Generated by Django 3.2.10 on 2022-01-06 17:59

from django.contrib.auth.models import AbstractUser
from django.db import migrations


def get_admins(apps, schema_editor):
    """add any superusers to the "admin" group"""

    db_alias = schema_editor.connection.alias
    groups = apps.get_model("auth", "Group")
    group = groups.objects.using(db_alias).get(name="admin")

    users = apps.get_model("bookwyrm", "User")
    admins = users.objects.using(db_alias).filter(is_superuser=True)

    for admin in admins:
        admin.groups.add(group)


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0123_alter_user_preferred_language"),
    ]

    operations = [
        migrations.RunPython(get_admins, reverse_code=migrations.RunPython.noop),
    ]
