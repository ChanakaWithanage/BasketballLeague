
from django.contrib import admin
from django.urls import re_path
from . import views
from django.conf.urls import include


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^about/$', views.about, name='about'),     # ex:- https:127.0.0.0/about
    re_path(r'^teams/', include('teams.urls')),
]
