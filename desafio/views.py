from django.shortcuts import render
from django.views import View


def indexView(request):
    return render(request, 'index.html' )