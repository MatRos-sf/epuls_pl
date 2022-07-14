from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("registration/", views.create_user, name='registration')
]