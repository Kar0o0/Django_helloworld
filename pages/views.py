from django.http import HttpResponse


def homepagepiew(request):
    return HttpResponse("Hello World!")
