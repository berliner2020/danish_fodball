"""fixtures URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.fixtures, name='fixtures'),
    path("<int:timestamp>", views.scores_by_timestamp),
    path("<str:date_word>", views.scores_by_word),
]
