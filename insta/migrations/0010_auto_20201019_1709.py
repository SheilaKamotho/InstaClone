# Generated by Django 2.0.2 on 2020-10-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_auto_20201019_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='comments',
            new_name='comment',
        ),
    ]
