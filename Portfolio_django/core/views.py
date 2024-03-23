from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def index(request):

    return JsonResponse({})

def home(request):

    return render(request, 'index.html')

@staff_member_required
def dashboard(request):

    return render(request, 'admin/admin.html')