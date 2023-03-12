"""scores URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path("today", views.today),
    path("<date>", views.scores),
]
