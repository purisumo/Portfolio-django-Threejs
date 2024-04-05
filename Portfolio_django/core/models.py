from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=255, blank=False, null=True)
    miname = models.CharField(max_length=1, blank=False, null=True)
    lname = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    social_link = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, blank=False, null=True)
    about_me = models.TextField(blank=True, null=True)
    picture = models.FileField(upload_to='profile/', blank=False, null=True)
    
    def __str__(self):
        return self.fname

    def save(self, *args, **kwargs):
        if self.pk is None and Profile.objects.exists():
            # Only allow one object to be created
            raise ValidationError("You can only create one Profile object")
        super().save(*args, **kwargs)

class Experience(models.Model):
    experience = models.TextField()


class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()

class ProjectImages(models.Model):
    image = models.FileField(upload_to="project_images")
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=64)

class Framework(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=64)