from django.contrib import admin
from django.urls import  path
from apps.curso.views import crearCurso

app_name = 'curso'

urlpatterns = [
    path('curso/crear/', crearCurso.as_view(), name='crear'),
]
