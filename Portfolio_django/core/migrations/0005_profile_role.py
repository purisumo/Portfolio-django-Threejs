# Generated by Django 5.0.2 on 2024-03-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(max_length=255, null=True),
        ),
    ]