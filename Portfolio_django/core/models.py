from django.db import models

# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=255, blank=False, null=True)
    miname = models.CharField(max_length=1, blank=False, null=True)
    lname = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    social_link = models.TextField(max_length=255, blank=True, null=True)
    about_me = models.TextField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.fname

class Experience(models.Model):
    experience = models.TextField(max_length=3000)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class ProjectImages(models.Model):
    image  = models.FileField(upload_to="project_image")
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)