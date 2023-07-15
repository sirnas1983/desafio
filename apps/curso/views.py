from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.curso.models import Curso



class crearCurso(CreateView):
    template_name = 'crear-curso.html'
    model = Curso
    field = ['nombre', 'duracion', 'fecha_inicio', 'disponibilidad']
    success_url = reverse_lazy('index')


