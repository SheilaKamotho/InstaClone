# Generated by Django 2.0.2 on 2020-10-19 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0020_remove_image_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Image'),
        ),
    ]
