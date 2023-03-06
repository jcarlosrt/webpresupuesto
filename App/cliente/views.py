from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.generic import ListView
from App.cliente.models import Basecliente


# Create your views here.


def iniciocliente(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'cliente/indexcli.html',
            {
                'title': 'Inicio Cliente',


             }
   )

class VerClientes(ListView):
    model=Basecliente
    template_name = 'cliente/indexcli.html'


