# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .csv2db import DbManager


def index(request):
    return HttpResponse("Hello, world. You're at the database tools index.")


def fill_databases(request):
    db_manager = DbManager()
    #db_manager.import_clients()
    db_manager.import_allergens()
    db_manager.import_ingredients()
    db_manager.import_sandwiches()
    return HttpResponse("... bazy wypełnione")


def clean_databases(request):
    db_manager = DbManager()
    db_manager.delete_clients()
    return HttpResponse("... bazy wyczyszczone")