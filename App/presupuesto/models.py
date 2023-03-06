from django.db import models
from App.cliente.models import Basecliente,prevision


# Create your models here.
class TipoProcedimiento(models.Model):
    tipo_proced=models.CharField(max_length=30, verbose_name="tipo de procedimientos")




class presupuesto(models.Model):
    n_presup=models.IntegerField(null=False,blank=False, verbose_name="Num de presupuesto")
    sub_presu=models.IntegerField(null=False,blank=False, verbose_name="sub presupuesto", default=1)
    fecha_presu=models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    fecha_modif_presu=models.DateTimeField(auto_now=True, verbose_name="ultima modificación")
    fecha_hospi=models.DateField (null=True, blank=True, verbose_name="Fecha probable de intervención")
    Rut_cliente=models.ForeignKey(Basecliente,null=True,blank=True,on_delete=models.RESTRICT)
    tipo_proced=models.ForeignKey(TipoProcedimiento,null=True,blank=True,on_delete=models.RESTRICT)
    prevision=models.ForeignKey(prevision,blank=True,null=True,on_delete=models.RESTRICT)
    medico_tratante=models.CharField(max_length=200, verbose_name="Medico Tratante")
    especialidad_med=models.CharField(max_length=100)
    fl_cot_selec=models.BooleanField(default=False, verbose_name="cotizacion seleccionada")
    fl_pres_actualizado=models.BooleanField(default=False, verbose_name="presupuesto modificado")
    fl_presu_enviado=models.BooleanField(default=False)
    

