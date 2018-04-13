from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def pre_index(request):
    return render(request, "index.html")

def pre_bio(pre_bio):
	return render(pre_bio, "bio.html")

def pre_profile(pre_profile):
	return render(pre_profile, "profile.html")

def pre_services(pre_services):
	return render(pre_services, "services.html")

def pre_projects(pre_projects):
	return render(pre_projects, "projects.html")

