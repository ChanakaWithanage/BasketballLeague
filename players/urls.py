
from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^about/$', views.about, name='about'),     # ex:- https:127.0.0.0/about
]
