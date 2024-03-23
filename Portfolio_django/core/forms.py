from django import forms
from .models import Profile, Experience, Projects, ProjectImages

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'miname', 'lname', 'email', 'number', 'social_link', 'about_me']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['experience']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name', 'description', 'link']

class ProjectImagesForm(forms.ModelForm):
    class Meta:
        model = ProjectImages
        fields = ['image', 'project']  # Specify the fields to be displayed in the form
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),  # Allow multiple file selection
        }
