from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Projects)

# Register your models here.
