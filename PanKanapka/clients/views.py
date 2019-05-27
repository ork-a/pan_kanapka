from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def logout_view(request):
    logout(request)
    messages.info(request, "Zostałeś poprawnie wylogowany")
    return HttpResponseRedirect(request.GET.get('next', '/'))


@login_required()
def login_view(request):
    messages.info(request, "Zostałeś poprawnie zalogowany")
    next_page = request.POST.get('next', '/')
    return HttpResponseRedirect(next_page)
