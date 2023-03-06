from django.db import models

# Create your models here.


class pabellon(models.Model):
    cod_pabellon=models.CharField(max_length=5,null=False, blank=False, verbose_name="codigo pabellon")
    cod_fns_pabellon = models.CharField(max_length=3, null=True,blank=True, verbose_name="pabellon FONASA")
    desc_pabellom =models.CharField(max_length=100, null=True, blank=True, verbose_name="Descripcion del pabellon")
    ambito_pabellon=models.CharField(max_length=100)
    tipo_pabellon=models.CharField(max_length=100)
    valor_pabellon=models.IntegerField(null=False, blank=False)

class codificacion(models.Model):
    cod_fns=models.CharField(max_length=10)
    glosa_fns=models.CharField(max_length=300)
    cod_int=models.CharField(max_length=15)
    glosa_clinica=models.CharField(max_length=300)
    pabellon_fns=models.CharField(max_length=3,null=True, blank=True)
    cod_pab_clinica=models.ForeignKey(pabellon.cod_pabellon,null=True,blank=True,on_delete=models.RESTRICT)

