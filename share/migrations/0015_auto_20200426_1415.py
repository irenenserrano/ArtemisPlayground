# Generated by Django 3.0.4 on 2020-04-26 21:15

from django.db import migrations, models
import share.models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0014_auto_20200426_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ImageField(upload_to=share.models.user_directory_path),
        ),
    ]
