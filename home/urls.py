from django.contrib import admin
from django.urls import path, include
from home import views


admin.site.site_header = "Log in to vikas admin"
admin.site.site_title = 'Welcome'
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact')
]
