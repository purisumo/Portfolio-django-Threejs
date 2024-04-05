from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/create/', profile_create, name='profile-create'),
    path('dashboard/<int:pk>/update/', profile_update, name='profile-update'),
    path('dashboard/exp_create/', exp_create, name='exp-create'),
    path('dashboard/<int:pk>/exp_update/', exp_update, name='exp-update'),
    path('dashboard/<int:pk>/exp_delete/', exp_delete, name='exp-delete'),
    path('dashboard/project_create/', project_create, name='project-create'),
    path('dashboard/<int:pk>/project_update/', project_update, name='project-update'),
    path('dashboard/<int:pk>/project_delete/', project_delete, name='project-delete'),
    path('dashboard/language-skill/', language_skill, name='language_skill'),
    path('dashboard/<int:pk>/language_update/', language_update, name='language_update'),
    path('dashboard/<int:pk>/language_delete/', language_delete, name='language_delete'),
    path('dashboard/framework-skill/', framework_skill, name='framework_skill'),
    path('dashboard/<int:pk>/framework_update/', framework_update, name='framework_update'),
    path('dashboard/<int:pk>/framework_delete/', framework_delete, name='framework_delete'),
    path('dashboard/Skills/', skills, name='skills'),
]