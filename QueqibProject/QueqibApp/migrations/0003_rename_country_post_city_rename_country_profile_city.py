# Generated by Django 4.0.4 on 2022-06-11 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueqibApp', '0002_rename_countries_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='country',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='country',
            new_name='city',
        ),
    ]
