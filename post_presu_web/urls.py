"""post_presu_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from App.post.api.router import router_posts
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from App.seguiweb import forms, views
from App.seguiweb.views import ListaRequerimientos2
from App.seguiweb.views import EditarRequerimiento
from App.seguiweb.views import IngresoRequerimiento

from App.seguiweb.views import eventos



urlpatterns = [

    path('', views.home, name='home'),
    path('cliente/',include("App.cliente.urls")),
    path('presupuesto/',include("App.presupuesto.urls")),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
             (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),


    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('api/',include(router_posts.urls)),
    path('seguiweb/requerimientos/', ListaRequerimientos2.as_view(), name='requirementos'),
    path('seguiweb/requerimientos2/', views.requerimientos2, name='requirementos2'),
    path('seguiweb/gestion_reque/<id_cliente>', views.gestion_reque, name='gestion_reque'),
    path('seguiweb/editar_requeri/<pk>', EditarRequerimiento.as_view(), name='editar_requeri'),
    path('seguiweb/ingreso_presu/', IngresoRequerimiento.as_view(), name='ingreso_presu'),
    path('seguiweb/eventos/<id_cliente>', views.eventos, name='eventos'),






]