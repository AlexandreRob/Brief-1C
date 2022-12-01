from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import csv
from .models import *


def home(request):
    return render(request, "home.html", {})


def import_csv(request):
    return render(request, "import.html", {})

# Create your views here.
