from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

from py_twitter_accidents.accidents import views

urlpatterns = [
    path('', views.accidents, name='accidents'),
]