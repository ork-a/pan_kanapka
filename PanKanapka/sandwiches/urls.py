from django.urls import path

from . import views

app_name = 'sandwiches'

urlpatterns = [
    path('', views.sandwiches, name='sandwiches'),
]
