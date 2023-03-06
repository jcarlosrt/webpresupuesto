from django.db import models
from App.seguiweb.choices import Isapre,Seguro_comple,Procedencia,Estado
from datetime import datetime




# Create your models here.

class Post(models.Model):
    Procedencia=models.CharField(max_length=100,blank=True,null=True,choices=Procedencia)
    Procedencia_key=models.IntegerField(blank=True,null=True)
    IpAddress=models.CharField(max_length=15,blank=True,null=True)
    StartedOn=models.DateTimeField(blank=True,null=True, default=datetime.now )
    SubmittedOn=models.DateTimeField(blank=True,null=True)
    UserId=models.CharField(max_length=37,blank=True,null=True)
    UserProvider=models.CharField(max_length=50,blank=True, null=True)
    Username=models.CharField(max_length=50,null=True,blank=True)
    ClassId=models.CharField(max_length=20,blank=True,null=True)
    ReferralCode=models.CharField(max_length=10,blank=True,null=True)
    Language=models.CharField(max_length=10,blank=True,null=True)
    SourceSiteId=models.CharField(max_length=37,blank=True,null=True)
    SourceSiteDisplayName=models.CharField(max_length=37,blank=True,null=True)
    ApplicationName=models.CharField(max_length=30,blank=True,null=True)
    DateCreated=models.DateTimeField(blank=True,null=True)
    Description=models.CharField(max_length=250,blank=True,null=True)
    ExpirationDate=models.DateTimeField(blank=True,null=True)
    Web_key=models.CharField(max_length=37,blank=True,null=True)
    LastModified=models.DateTimeField(blank=True,null=True)
    Owner=models.CharField(max_length=37,blank=True,null=True)
    PublicationDate=models.DateTimeField(blank=True,null=True)
    Status=models.CharField(max_length=30,blank=True,null=True)
    Title=models.CharField(max_length=150,blank=True,null=True)
    Visible=models.CharField(max_length=5,blank=True,null=True)
    SourceKey=models.CharField(max_length=150,blank=True,null=True)
    Ingresa_el_nombre_de_tu_Isapre=models.CharField(max_length=150,blank=True,null=True)
    Apellido=models.CharField(max_length=150,blank=True,null=True)
    Fecha_probable_de_Hospitalizacion=models.CharField(max_length=150, blank=True,null=True)
    Nombre_de_la_intervencion=models.CharField(max_length=150,blank=True,null=True)
    Pasaporte=models.CharField(max_length=150, blank=True,null=True)
    Apellido_Paterno=models.CharField(max_length=200,blank=True,null=True)
    Seguro_complementario=models.CharField(max_length=150,blank=True,null=True, choices=Seguro_comple)
    Apellido_Materno=models.CharField(max_length=150,blank=True,null=True)
    Telefono_movil=models.CharField(max_length=30,blank=True,null=True)
    Isapre=models.CharField(max_length=150,blank=True,null=True,choices=Isapre)
    Ingresa_el_nombre_de_tu_Seguro_Complementario=models.CharField(max_length=150,blank=True,null=True)
    Adjuntar_orden_medica=models.CharField(max_length=250,blank=True,null=True)
    Telefono_fijo=models.CharField(max_length=50,blank=True,null=True)
    Solicitar_el_presupuesto_utilizando=models.CharField(max_length=50,blank=True,null=True)
    Codigo_de_intervencion=models.CharField(max_length=50,blank=True,null=True)
    RUT=models.CharField(max_length=50,blank=True,null=True)
    Email_de_contacto=models.CharField(max_length=150,blank=True,null=True)
    Nombre=models.CharField(max_length=200,blank=True,null=True)
    Tu_telefono_de_contacto_es=models.CharField(max_length=50,blank=True,null=True)
    Fecha_de_nacimiento=models.DateTimeField(blank=True,null=True)
    Medico_tratante=models.CharField(max_length=200,blank=True,null=True)
    pri_contac=models.BooleanField(blank=True,null=True)
    F_primer_contac=models.DateTimeField(blank=True,null=True)
    observacion_primercont=models.TextField(max_length=500,blank=True,null=True)
    envio_presu=models.BooleanField(default=False, blank=True,null=True)
    fecha_envio_presu=models.DateTimeField(blank=True, null=True)
    observacion_envio_presu=models.TextField(max_length=500,blank=True,null=True)
    fecha_y_hora_estimada_hospitalizacion_por_presu=models.DateTimeField(blank=True, null=True)
    fecha_y_hora_confirmada_hospitalizacion=models.DateTimeField(blank=True, null=True)
    Estado_requerimiento=models.CharField(max_length=2, blank=True,null=True,choices=Estado,default='PE')


    def __str__(self):
        texto = "{} - {} - {} "
        return texto.format(self.id, self.Nombre,self.RUT
                        )


