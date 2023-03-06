from django.db import models
from .choices import sexo

# Create your models here.

class comuna(models.Model):
    cod_comuna=models.CharField(blank=False, null=False, max_length=6)
    nom_comuna=models.TextField(blank=False, null=False,max_length=100)
    def __str__(self):
        texto = "{} - {} "
        return texto.format(self.cod_comuna, self.nom_comuna)


class provincia (models.Model):
    cod_provincia=models.CharField(blank=False, null=False, max_length=5)
    nom_provincia=models.TextField(blank=False, null=False,max_length=100)
    def __str__(self):
        texto = "{} - {} "
        return texto.format(self.cod_provincia, self.nom_provincia)


class region(models.Model):
    cod_region=models.CharField(blank=False, null=False, max_length=5)
    nom_region=models.TextField(blank=False, null=False,max_length=100)
    def __str__(self):
        texto = "{} - {} "
        return texto.format(self.cod_region, self.nom_region
                        )


class pais(models.Model):
    cod_pais=models.CharField(blank=False, null=False, max_length=5)
    nom_pais=models.TextField(blank=False, null=False,max_length=100)
    abre_pais = models.CharField(blank=False, null=False, max_length=4)

    def __str__(self):
        texto = "{} - {} -{}"
        return texto.format(self.cod_pais, self.nom_pais, self.abre_pais
                        )


class prevision(models.Model):
    cod_prevision=models.CharField(max_length=2)
    prevision_nom=models.CharField(max_length=100)
    def __str__(self):
        return "{} - {}". format(self.cod_prevision, self.prevision)


class estadocivil(models.Model):
    cod_estadocivil=models.CharField(max_length=2)
    estadocivil=models.CharField(max_length=100)
    def __str__(self):
        return "{} - {}". format(self.cod_estadocivil, self.estadocivil)


class sexo(models.Model):
    cod_sexo=models.CharField(blank=False, null=False, max_length=2)
    letra_sexo=models.CharField(blank=False, null=False, max_length=2)
    nom_sexo=models.TextField(blank=False, null=False,max_length=100)
    def __str__(self):
        texto = "{} - {} - {}"
        return texto.format(self.cod_sexo, self.letra_sexo,self.nom_sexo
                            )

class Basecliente(models.Model):
    id2cliente = models.IntegerField(blank=True, null=True, verbose_name="numero de presupuesto")
    rut=models.CharField(blank=True, null=True, max_length=11, verbose_name="RUT")
    nombre=models.TextField(blank=True, null=True, max_length=200, verbose_name="Nombres")
    appaterno=models.TextField(blank=True, null=True, max_length=100, verbose_name="Apellido Paterno")
    apmaterno=models.TextField(blank=True, null=True, max_length=100, verbose_name="Apellido Materno")
    sexo =models.ForeignKey(sexo,on_delete=models.RESTRICT,blank=True, null=True )
    fechanacimiento=models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    Nacionalidad = models.ForeignKey(pais,on_delete=models.RESTRICT,blank=True, null=True )
    estadocivil = models.ForeignKey(estadocivil,on_delete=models.RESTRICT,blank=True, null=True, verbose_name="Estado Civil" )
    direccion =models.TextField(blank=True, null=True, max_length=200)
    region = models.ForeignKey(region,on_delete=models.RESTRICT, blank=True, null=True)
    provincia = models.ForeignKey(provincia,on_delete=models.RESTRICT, blank=True, null=True)
    comuna = models.ForeignKey(comuna,on_delete=models.RESTRICT, blank=True, null=True)
    ciudad = models.TextField(blank=True, null=True, max_length=150, verbose_name="Ciudad")
    fonomovil = models.TextField(blank=True, null=True, max_length=20, verbose_name="celular")
    fonofijo = models.TextField(blank=True, null=True, max_length=20, verbose_name="Telefono Fijo")
    email = models.TextField(blank=True, null=True, max_length=30)
    prevision = models.ForeignKey(prevision,on_delete=models.RESTRICT, blank=True, null=True)
    ppn=models.IntegerField(blank=True, null=True)




    def nombre_completo (self):
        return "{} {} {}". format(self.nombre, self.appaterno, self.apmaterno)

    def __str__(self):
        return self.nombre_completo()









