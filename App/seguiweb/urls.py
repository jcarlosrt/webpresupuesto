from django.urls import path
from App.seguiweb.views import ListaRequerimientos2


urlpatterns = [
    path('requerimientos2/', ListaRequerimientos2.as_view(), name='requirementos2')
    ]