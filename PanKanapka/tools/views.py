from django.shortcuts import render
from django.http import HttpResponse
from .csv2db import DbFromCsvImporter

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tools index.")

def fill_databases(request):
    importer = DbFromCsvImporter()
    importer.ImportClients()
    return HttpResponse("... bazy wypełnione")