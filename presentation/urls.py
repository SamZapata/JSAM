from django.urls import path
from django.conf.urls import url
from . import views 

urlpatterns = [
	path('', views.pre_index, name='index'),
	path('index', views.pre_index, name='index'),
	path('bio', views.pre_bio, name='pre_bio'),
	path('profile', views.pre_profile, name='pre_profile'),
	path('services', views.pre_services, name='pre_services'),
	path('projects', views.pre_projects, name='pre_projects'),
	#url(r'^$', views.index, name='index'),
	#url(r'^$blog/post', views.post, name='post'),
]