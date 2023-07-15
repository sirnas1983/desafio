from django.shortcuts import render
from django.views import View

from apps.curso.models import Curso


def indexView(request):
    context = {
        'posteos' : Curso.objects.all()}
    return render(request, 'index.html', context )