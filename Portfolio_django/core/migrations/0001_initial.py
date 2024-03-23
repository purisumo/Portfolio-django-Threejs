# Generated by Django 5.0.2 on 2024-03-23 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255, null=True)),
                ('miname', models.CharField(max_length=1, null=True)),
                ('lname', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('social_link', models.TextField(blank=True, max_length=255, null=True)),
                ('about_me', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(max_length=3000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('link', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='project_image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.projects')),
            ],
        ),
    ]