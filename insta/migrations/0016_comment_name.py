# Generated by Django 2.0.2 on 2020-10-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0015_auto_20201019_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]