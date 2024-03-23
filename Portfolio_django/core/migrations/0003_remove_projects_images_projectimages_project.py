# Generated by Django 5.0.2 on 2024-03-23 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_projectimages_project_projects_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='images',
        ),
        migrations.AddField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.projects'),
            preserve_default=False,
        ),
    ]
