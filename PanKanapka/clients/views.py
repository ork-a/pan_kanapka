from django.http import HttpResponse


def clients(request):
    return HttpResponse("Clients here")
