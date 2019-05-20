# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .csv2db import DbManager


def index(request):
    return HttpResponse("Hello, world. You're at the database tools index.")


def fill_databases(request):
    return HttpResponse("Użyj >>python manage.py filldb<< z linii poleceń")


def clean_databases(request):
    return HttpResponse("Użyj >>python manage.py cleandb<< z linii poleceń")