# Generated by Django 2.2.6 on 2019-12-04 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20191204_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
    ]