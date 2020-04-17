# Generated by Django 3.0.4 on 2020-04-17 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('share', '0005_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_header', models.CharField(blank=True, max_length=50)),
                ('post_body', models.TextField(blank=True, max_length=500)),
                ('post_created', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now=True)),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
