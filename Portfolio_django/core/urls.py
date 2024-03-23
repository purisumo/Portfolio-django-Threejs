from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
]