# Generated by Django 4.1.2 on 2022-12-01 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_username_clients_client"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clients",
            old_name="client",
            new_name="username",
        ),
    ]
