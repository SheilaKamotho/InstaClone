# Generated by Django 2.0.2 on 2020-10-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0016_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Comment'),
        ),
    ]
