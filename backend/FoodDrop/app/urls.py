from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^get', views.get_openings, name='open'),
        url(r'^login', views.login_user, name='login'),
        url(r'^register', views.create_auth, name='register'),
]
