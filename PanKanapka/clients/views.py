from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import User


def logout_view(request):
    logout(request)
    messages.info(request, "Zostałeś poprawnie wylogowany")
    return HttpResponseRedirect(request.GET.get('next', '/'))

def add_new_user(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('dziala')
    else:
        return render(request, 'add_new_user.html',{
            'form': form
        })


@login_required()
def login_view(request):
    messages.info(request, "Zostałeś poprawnie zalogowany")
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)
