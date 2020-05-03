# Generated by Django 3.0.3 on 2020-05-03 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import share.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coder_yet', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200, unique=True)),
                ('video', models.BooleanField(default=False)),
                ('thumb_nail', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to=share.models.user_directory_path)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='myproblems/')),
                ('discipline', models.CharField(max_length=50)),
                ('make_public', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('coder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Coder')),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('code', models.TextField(max_length=10000)),
                ('url', models.URLField(blank=True, max_length=300)),
                ('input', models.TextField(blank=True, max_length=100)),
                ('output', models.TextField(blank=True, max_length=100)),
                ('make_public', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='myscripts/')),
                ('working_code', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('coder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Coder')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(blank=True, max_length=50)),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_header', models.CharField(blank=True, max_length=50)),
                ('post_body', models.TextField(blank=True, max_length=500)),
                ('post_created', models.DateTimeField(auto_now_add=True)),
                ('post_updated', models.DateTimeField(auto_now=True)),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Media')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.Photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_created', models.DateTimeField(auto_now_add=True)),
                ('comment_updated', models.DateTimeField(auto_now=True)),
                ('comment_body', models.TextField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Post')),
            ],
        ),
    ]
