

from django.db import models
from App.post.models import Post




# Create your models here.

class Eventos(models.Model):
    tipo_evento=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        texto = "{} "
        return texto.format(self.tipo_evento)



class Seguimientos(models.Model):
    ticket_presupuesto=models.ForeignKey(Post,null=False, blank=True, on_delete=models.CASCADE)
    tipo_evento=models.ForeignKey(Eventos,null=False, blank=False, on_delete=models.PROTECT)
    texto_evento=models.TextField(max_length=1500,null=False, blank=False)
    # Fecha evento
    def eventos(self):
        return self.todo_eventos.all()

    def __str__(self):
        texto = " {} - {} - {}"
        return texto.format(self.ticket_presupuesto_id, self.tipo_evento,self.texto_evento)



