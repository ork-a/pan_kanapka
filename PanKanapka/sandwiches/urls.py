from django.urls import path

from . import views

app_name = 'sandwiches'

urlpatterns = [
    path('', views.sandwiches, name='sandwiches'),
    path('nowa-kanapka', views.create_sandwich, name='create_sandwich'),
    path('moja-kanapka', views.new_sandwich, name='new_sandwich'),
    path('potwierdz-nowa-kanapke', views.confirm_new_sandwich, name='confirm_new_sandwich'),
]
