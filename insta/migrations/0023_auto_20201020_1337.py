# Generated by Django 2.0.2 on 2020-10-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0022_auto_20201019_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image1',
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Comment'),
        ),
    ]