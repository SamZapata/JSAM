from django.urls import path
from django.conf.urls import url
from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('bio', views.bio, name='bio'),
	path('profile', views.profile, name='profile'),
	path('services', views.services, name='services'),
	path('projects', views.projects, name='projects'),
	#url(r'^$', views.index, name='index'),
	#url(r'^$blog/post', views.post, name='post'),
]