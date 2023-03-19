"""scores URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:timestamp>", views.scores_by_timestamp),
    path("<str:date_word>", views.scores_by_word, name="fixtures"),
]
