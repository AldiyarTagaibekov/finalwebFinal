# Generated by Django 2.2.6 on 2019-11-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures'),
        ),
    ]
