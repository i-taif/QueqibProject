# Generated by Django 4.0.4 on 2022-06-13 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueqibApp', '0008_comment_slug_post_slug_alter_city_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
