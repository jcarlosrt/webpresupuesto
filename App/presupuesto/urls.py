from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciopresupuesto, name="inicio_presu")



]
