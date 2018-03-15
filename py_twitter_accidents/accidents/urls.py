from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

from py_twitter_accidents.core import views

urlpatterns = [
    path('', views.home, name='home'),
]