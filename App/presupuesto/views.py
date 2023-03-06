from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.


def iniciopresupuesto(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'presupuesto/indexpresu.html',
        {
            'title': 'Inicio Presupuesto',


        }
    )


