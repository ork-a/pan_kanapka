from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User


def logout_view(request):
    logout(request)
    messages.info(request, "Zostałeś poprawnie wylogowany")
    return HttpResponseRedirect(request.GET.get('next', '/'))

def home_page_view(request):
    return render(request, 'add_new_user.html')

@login_required()
def login_view(request):
    messages.info(request, "Zostałeś poprawnie zalogowany")
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)


def registration_form(request):
    if request.method == 'POST':
        user = User(email='ppp@pp.pl', name='ppp')
        user.save()