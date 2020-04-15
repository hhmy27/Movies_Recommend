from django.shortcuts import render

from django.http import HttpResponse,request


# Create your views here.

def index(request):
    # return HttpResponse("ok")
    return render(request, 'movie/index.html')