from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filldb/', views.fill_databases, name='Wypełnianie bazy przykładowymi danymi')
]