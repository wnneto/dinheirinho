# Generated by Django 3.2 on 2022-06-04 10:33

from django.db import migrations
import nkpro.base.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', nkpro.base.models.UserManager()),
            ],
        ),
    ]