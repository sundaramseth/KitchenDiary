from django.views import generic
from django.shortcuts import render


def index(request):
    return render(request, 'kitchen/index.html')


def method(request):
    return render(request, 'method/method.html')
