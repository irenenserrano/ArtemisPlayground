# Generated by Django 3.0.4 on 2020-05-02 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_remove_user_following'),
        ('share', '0018_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
