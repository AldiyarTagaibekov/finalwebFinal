# Generated by Django 2.2.6 on 2019-12-04 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20191205_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_reaction',
        ),
    ]
