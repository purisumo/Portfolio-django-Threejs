# Generated by Django 4.2 on 2024-04-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_about_me_alter_profile_social_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experience',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(),
        ),
    ]
