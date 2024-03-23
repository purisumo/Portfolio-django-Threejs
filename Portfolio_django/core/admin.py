from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Projects)

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    form = ProjectImagesForm
# Register your models here.
