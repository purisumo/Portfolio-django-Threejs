from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from django.core.files.storage import default_storage
import os
from django.utils.text import slugify

from .models import *
from .forms import *
# Create your views here.
def index(request):

    return JsonResponse({})

def home(request):
    skills = Language.objects.all()
    framework = Framework.objects.all()
    profile = Profile.objects.get(pk=1)
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    projects_images = ProjectImages.objects.all()
    context = {
        'profile': profile,
        'experience': experience,
        'projects': projects,
        'projects_images': projects_images,
        'skills':skills,
        'framework':framework,

    }
    return render(request, 'index.html', context)

@staff_member_required
def dashboard(request):
    profile = get_object_or_404(Profile, pk=1)
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    projects_images = ProjectImages.objects.all()
    context = {
        'profile': profile,
        'experience': experience,
        'projects': projects,
        'projects_images': projects_images,

    }
    return render(request, 'dashboard/admin.html', context)



##########Proifile######################




def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            return redirect('profile-create')
    else:
        form = ProfileForm()
    return render(request, 'profile-cms.html', {'form': form})


def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    picture_name = "Avatar.png"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        old_filename = profile.picture.name
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, old_filename)):
            os.remove(os.path.join(settings.MEDIA_ROOT, old_filename))
        if form.is_valid():
            pro = form.save(commit=False)
            profile.picture = pro.picture
            pro.picture.name = picture_name
            pro.save()    
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile-cms.html', {'form': form, 'profile':profile})


############Experience############



def exp_create(request):
    experience = Experience.objects.all()
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exp-create')
    else:
        form = ExperienceForm()
    return render(request, 'profile-cms.html', {'form': form,'experience':experience})

def exp_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('exp-create')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'profile-cms.html', {'form': form})

def exp_delete(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    exp.delete()

    return redirect(request.META['HTTP_REFERER'])




# ###################Projects####################################



def project_create(request):
    projects = Projects.objects.all()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        image_form = ProjectImagesForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            project = form.save(commit=False)
            project.save() 

            for image in request.FILES.getlist('image'):
                ProjectImages.objects.create(image=image, project=project)

            return redirect('project-create')

    else:
        form = ProjectsForm()
        image_form = ProjectImagesForm()

    return render(request, 'profile-cms.html', {'form': form, 'image_form': image_form, 'projects': projects})

def project_update(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        image_form = ProjectImagesForm(request.POST, request.FILES, instance=project)
        print(image_form)
        if form.is_valid() and image_form.is_valid():
            project = form.save(commit=False)
            project.save() 

            project_images = ProjectImages.objects.filter(project=project)
            for image in project_images:
                file_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
                if default_storage.exists(file_path):
                    default_storage.delete(file_path)
                image.delete()
                
            for image in request.FILES.getlist('image'):
                ProjectImages.objects.create(image=image, project=project)

            return redirect('project-create')
    else:
        form = ProjectsForm(instance=project)
        image_instance = project.projectimages_set.first()
        print(image_instance)
        if image_instance:
            initial_data = {'image': image_instance.image}
            image_form = ProjectImagesForm(instance=project, initial=initial_data)
        else:
            image_form = ProjectImagesForm(instance=project)
    return render(request, 'profile-cms.html', {'form': form, 'image_form': image_form, 'project':project})

def project_delete(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    project_images = ProjectImages.objects.filter(project=project)
    for image in project_images:
        file_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
        if default_storage.exists(file_path):
            default_storage.delete(file_path)
        image.delete()
    project.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def skills(request):
    language = Language.objects.all()
    framework = Framework.objects.all()

    context = {
        'language':language,
        'framework':framework,
    }
    return render(request, 'profile-cms.html', context)

def language_skill(request):
    if request.method == "POST":
        form = LanguageSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = LanguageSkillForm()
    return render(request, 'profile-cms.html', {'form':form})

def language_update(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == 'POST':
        form = LanguageSkillForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = LanguageSkillForm(instance=language)
    return render(request, 'profile-cms.html', {'form': form})

def language_delete(request, pk):
    language = get_object_or_404(Language, pk=pk)
    language.delete()

    return redirect(request.META['HTTP_REFERER'])

def framework_skill(request):
    if request.method == 'POST':
        form = FrameworkSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = FrameworkSkillForm()
    return render(request, 'profile-cms.html', {'form':form})

def framework_update(request, pk):
    framework = get_object_or_404(Framework, pk=pk)
    if request.method == 'POST':
        form = FrameworkSkillForm(request.POST, instance=framework)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = FrameworkSkillForm(instance=framework)
    return render(request, 'profile-cms.html', {'form': form})

def framework_delete(request, pk):
    framework = get_object_or_404(Framework, pk=pk)
    framework.delete()

    return redirect(request.META['HTTP_REFERER'])