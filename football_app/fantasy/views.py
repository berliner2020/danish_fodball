from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime


# Create your views here.
def index(request):
    return HttpResponse("<h1>Superliga Fantasy</h1>")

