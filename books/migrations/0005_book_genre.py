# Generated by Django 2.2.6 on 2019-11-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191109_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]