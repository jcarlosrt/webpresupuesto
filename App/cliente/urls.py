from django.urls import path
from . import views
from App.cliente.views import VerClientes

urlpatterns = [
    path('', VerClientes.as_view(), name="inicio_cliente" )



]
