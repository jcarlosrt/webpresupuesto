"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from App.post.models import Post
from App.seguiweb.models import Seguimientos
from App.seguiweb.choices import Procedencia
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.html import format_html
from django.urls import reverse_lazy
from App.seguiweb.forms import ingresoform, editarform
from App.cliente.views import iniciocliente




def home(request):
    """Renders the home page."""

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Inicio',
            'year': datetime.now().year,

        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def requerimientos2(request):
    if not request.user.is_authenticated:
        return render(request, 'app/indexsegu.html')

    """Renders the home page."""
    entity = Post.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(entity, 5)
        entity = paginator.page(page)
    except:
        raise Http404

    cantidad = Post.objects.all().count()
    id_cliente = Post.objects.filter(id=1)

    assert isinstance(request, HttpRequest)

    data = {
        'title': 'requerimientos',
        'year': datetime.now().year,
        'listado': entity,
        'cantidad': cantidad,
        'paginator': paginator,
        'id_cliente': id_cliente,

    }

    return render(request,
                  #       'app/requerimientos.html',{'title':'requerimientos','year':datetime.now().year,"listado":entity, "cantidad":cantidad, "paginator":paginator,}
                  'seguiweb/requerimientos3.html', data
                  )


def gestion_reque(request, id_cliente):
    id_cliente = Post.objects.filter(id=id_cliente)

    if not request.user.is_authenticated:
        return render(request, 'app/login.html')

    data = {
        'title': 'ver requerimiento',
        'year': datetime.now().year,
        'id_cliente': id_cliente,
    }

    return render(
        request,
        'seguiweb/gestionar_requeri.html', data

    )


class ListaRequerimientos2(LoginRequiredMixin, ListView):
    login_url = ('login')
    model = Post
    paginate_by = 5
    queryset = Post.objects.exclude(Estado_requerimiento ='CE').order_by('-id')


    template_name = 'seguiweb/requerimientos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Requerimientos Pendientes'
        context['cantidad'] = Post.objects.filter(envio_presu=False).count()
        return context

    def coloreado(self):
        return format_html('<h2 style ="color:blue;">{0}</h2>'.format(self.title))

class EditarRequerimiento(UpdateView,ListView):
    login_url = ('login')
    model = Post
    form_class = editarform
    template_name = 'seguiweb/editar_requeri.html'
    success_url = reverse_lazy('home')
    choices = Procedencia





class IngresoRequerimiento(CreateView,ListView):
    login_url = ('login')
    model = Post
    form_class = ingresoform
    template_name = 'seguiweb/ingreso_presu.html'
    success_url = reverse_lazy('ingreso_presu')
    paginate_by = 5
    queryset = Post.objects.exclude(Estado_requerimiento ='CE').order_by('-id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingreso Manual de Presupuesto'
        context['cantidad']=Post.objects.filter(envio_presu=False).count()
        return context


def eventos(request, id_cliente):
    eventos = Seguimientos.objects.all()
    lista_eventos = Seguimientos.objects.filter(id=id_cliente)


    if not request.user.is_authenticated:
        return render(request, 'seguiweb/login.html')

    data = {
        'title': 'eventos',
        'year': datetime.now().year,
        'eventos': eventos,
        'lista_eventos':lista_eventos,
        'ticket': id_cliente,


    }

    return render(
        request,
        'seguiweb/gestionar_eventos.html', data

    )


def iniciocliente(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cliente/indexcli.html',
        {
            'title': 'Inicio Cliente',
            'year': datetime.now().year,

        }
    )


