from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, "index.html")

def bio(r_bio):
	return render(r_bio, "bio.html")

def profile(r_profile):
	return render(r_profile, "profile.html")

def services(r_services):
	return render(r_services, "services.html")

def projects(r_projects):
	return render(r_projects, "projects.html")

