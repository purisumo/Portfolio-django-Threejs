from django import forms
from django.forms import inlineformset_factory
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'miname', 'lname', 'email', 'number', 'picture', 'social_link', 'role', 'about_me']
        labels = {
            'fname': 'First Name',
            'miname': 'Middle Name',
            'lname': 'Last Name',
            'number': 'Phone Number',
            'picture': 'Profile Picture',
            'social_link': 'Social Link',
            'role': 'Role',
            'about_me': 'About Me',
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['experience']
        labels = {
            'experience': 'Experience'
        }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'description', 'link']
        labels = {
            'project_name': 'Project Name',
            'description': 'Description',
            'link': 'Link',
        }

class ProjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImages
        fields = ['image']
        labels = {
            'image': 'Image'
        }
        widgets = {
            'image': forms.FileInput(attrs={'multiple': True})
        }

class LanguageSkillForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'level']
        labels = {
            'name': 'Language name',
            'level': 'Proficiency Level (1-100)',
        }

class FrameworkSkillForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ['name', 'level']
        labels = {
            'name': 'Framework Name',
            'level': 'Proficiency Level (1-100)',
        }