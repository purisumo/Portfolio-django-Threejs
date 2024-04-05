# Generated by Django 4.2 on 2024-04-05 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_projectimages_project_projects_images_and_more'),
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
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.FileField(upload_to='project_images'),
        ),
    ]