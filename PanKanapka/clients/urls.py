from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    # path('', views.clients, name='clients'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]
